# Generated by Django 2.0 on 2018-05-30 21:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0005_movie_mov_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='comment_nums',
        ),
    ]