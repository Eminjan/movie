# Generated by Django 2.0 on 2018-06-02 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0014_auto_20180602_0056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='image',
            field=models.EmailField(default='', max_length=254, verbose_name='封面图'),
        ),
    ]