from datetime import datetime
from django.db import models
from users.models import UserProfile


# Create your models here.


class Mov_Tag(models.Model):
    tag_name = models.CharField(max_length=30,verbose_name='标签')

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.tag_name


class Star(models.Model):
    star = models.IntegerField(verbose_name='星级')

    class Meta:
        verbose_name = '电影星级'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{}'.format(self.star)


class AddTime(models.Model):
    add_time = models.DateTimeField(default=datetime.now,verbose_name='上映时间')

    class Meta:
        verbose_name = '上映时间'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{}年'.format(self.add_time)


class Movie(models.Model):
    name = models.CharField(max_length=30, verbose_name='片名')
    tag = models.ForeignKey(Mov_Tag, on_delete=models.CASCADE, verbose_name='标签')
    mov_times = models.IntegerField(default='', verbose_name='片长')
    region = models.CharField(default='', verbose_name='地区',max_length=30)
    star = models.ForeignKey(Star, on_delete=models.CASCADE,verbose_name='星级')
    image = models.URLField(default='', verbose_name='封面图')
    add_time = models.ForeignKey(AddTime,on_delete=models.CASCADE,verbose_name='上映时间')
    mov_url = models.URLField(default='',verbose_name='电影链接')
    play_nums = models.IntegerField(default=0, verbose_name='播放次数')
    desc = models.TextField(verbose_name='影片介绍', default='')

    class Meta:
        verbose_name = '电影'
        verbose_name_plural = verbose_name
        ordering = ['-add_time']

    def __str__(self):
        return self.name


