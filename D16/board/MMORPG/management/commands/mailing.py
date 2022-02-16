from django.core.management.base import BaseCommand, CommandError
from MMORPG.models import User, Post
from MMORPG.functions import mailing

class Command(BaseCommand):
    help = 'Рассылка всем подписчикам о последних постах (напоминаем про себя)'
    requires_migrations_checks = True

    # def add_arguments(self, parser):
    #     parser.add_argument('category', type=str)

    def handle(self, *args, **options):
        email_list = {}
        self.stdout.write('Вы правда хотите сделать рассылку по всем почтам ?')
        for user in User.objects.all():
            if user.email is not None and user.email != '':
                # email = input(f'{user.email}')
                email_list[user] = user.email
        answer = input('Type yes/no: ')

        if answer != 'yes':
            self.stdout.write(self.style.ERROR('Отменено'))# в случае неправильного подтверждения говорим, что в доступе отказано
            return

        try:
            query = Post.objects.all().order_by('-id')[:2] # задаем кол-во постов в рассылке
            for user,email in email_list.items():
                mailing(user,email,query)
            self.stdout.write(self.style.SUCCESS(f'Succesfully sent last posts to users mail'))
            return
        except User.DoesNotExist:
            self.stdout.write(self.style.ERROR(f'Could not find user {user}'))