# Generated by Django 2.0 on 2018-05-30 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0006_remove_movie_comment_nums'),
    ]

    operations = [
        migrations.CreateModel(
            name='Star',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stars', models.IntegerField(default=4, verbose_name='星级')),
            ],
            options={
                'verbose_name': '电影星级',
                'verbose_name_plural': '电影星级',
            },
        ),
    ]
