# Generated by Django 3.2.5 on 2021-07-04 15:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_rename_category_category_none'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='None',
            new_name='category',
        ),
    ]
