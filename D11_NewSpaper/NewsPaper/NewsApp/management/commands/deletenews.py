from django.core.management.base import BaseCommand, CommandError
from NewsApp.models import Post, Category, PostCategory


class Command(BaseCommand):
    help = 'Удалять все новости из какой-либо категории' # показывает подсказку при вводе "python manage.py <ваша команда> --help"
    requires_migrations_checks = True # напоминать ли о миграциях. Если тру — то будет напоминание о том, что не сделаны все миграции (если такие есть)

    def add_arguments(self, parser):
        parser.add_argument('category', type=str)


    # Работает!!
    def handle(self, *args, **options):

        answer = input(f'Вы правда хотите удалить все статьи в категории {options["category"]}? yes/no: ')
        try:
            category = Category.objects.get(category_name=options['category'])
            post_category = PostCategory.objects.filter(category_through = category) # нахожу обькты промежуточной таблицы которые имеют данную категорию
            for post in post_category: # прохожусь по обьектам
                Post.objects.filter(pk = post.post_through.id).delete() # фильтрую по айди поста!!
                self.stdout.write(self.style.SUCCESS(f'Succesfully deleted all news from category {category}'))
        except Post.DoesNotExist:
            self.stdout.write(self.style.ERROR(f'Could not find category'))



