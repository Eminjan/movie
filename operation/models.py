from datetime import datetime
from django.db import models
from users.models import UserProfile
from movie.models import Movie
# Create your models here.


class UserFavorite(models.Model):
    user = models.ForeignKey(UserProfile,verbose_name='用户',on_delete=models.CASCADE)
    fav_id = models.IntegerField(default=0,verbose_name='数据ID')
    add_time = models.DateTimeField(default=datetime.now,verbose_name='收藏时间')

    class Meta:
        verbose_name = '用户收藏'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '用户({0})收藏了{1} '.format(self.user, self.fav_id)


class MovieComments(models.Model):
    # 课程评论 涉及到两个外键
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, verbose_name="电影")
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name="用户")
    comment = models.CharField(max_length=200,verbose_name='评论')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = "电影评论"
        verbose_name_plural = verbose_name

    def __str__(self):
        return '用户({0})对于《{1}》 评论 :'.format(self.user, self.movie)
