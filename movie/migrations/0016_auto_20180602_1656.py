# Generated by Django 2.0 on 2018-06-02 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0015_auto_20180602_1655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='image',
            field=models.URLField(default='', verbose_name='封面图'),
        ),
    ]
