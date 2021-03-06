# Generated by Django 4.0.2 on 2022-02-04 13:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('NewsApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='category_name_en',
            field=models.CharField(max_length=64, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='category',
            name='category_name_ru',
            field=models.CharField(max_length=64, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='category',
            name='category_name_uk',
            field=models.CharField(max_length=64, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='post',
            name='author_en',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='NewsApp.author'),
        ),
        migrations.AddField(
            model_name='post',
            name='author_ru',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='NewsApp.author'),
        ),
        migrations.AddField(
            model_name='post',
            name='author_uk',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='NewsApp.author'),
        ),
        migrations.AddField(
            model_name='post',
            name='header_en',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='header_ru',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='header_uk',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='text_en',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='text_ru',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='text_uk',
            field=models.CharField(max_length=128, null=True),
        ),
    ]
