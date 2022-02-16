# from django.db import models
# from django.contrib.auth.models import User
# from .models import MyUser
# from django.db.models.signals import post_save,pre_save,post_delete
# from django.dispatch import receiver


# @receiver(pre_save,sender=MyUser)
# def do_something(sender, **kwargs):
# 	if kwargs.get('created', False):
# 		instance = kwargs['instance']
# 		instance.automatic_value = instance.slug + str(instance.float) + str(instance.time)
# 		instance.save()

# post_save.connect(do_something, sender=MyUser)