# Generated by Django 2.0 on 2018-05-28 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0002_auto_20180528_2043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='mov_times',
            field=models.IntegerField(default='', verbose_name='片长'),
        ),
    ]