# Generated by Django 3.2.5 on 2021-07-08 09:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0012_remove_author_pesonal_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='username',
            new_name='author_name',
        ),
    ]
