from django.contrib import admin
from .models import UserFavorite, MovieComments


# Register your models here.

class UserFavoriteAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'fav_id', 'add_time']
    list_display_links = ['user', 'fav_id', 'add_time']
    list_filter = ['id', 'user', 'fav_id', 'add_time']


class MovieCommentsAdmin(admin.ModelAdmin):
    list_display = ['id', 'movie', 'user', 'add_time']
    list_filter = ['movie', 'user', 'add_time']


admin.site.register(UserFavorite, UserFavoriteAdmin)
admin.site.register(MovieComments, MovieCommentsAdmin)
