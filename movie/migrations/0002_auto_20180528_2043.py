# Generated by Django 2.0 on 2018-05-28 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='desc',
            field=models.TextField(default='', verbose_name='影片介绍'),
        ),
    ]