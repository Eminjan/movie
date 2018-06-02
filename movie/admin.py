from django.contrib import admin
from .models import Movie,Mov_Tag,Star,AddTime
# Register your models here.


class Mov_TagAdmin(admin.ModelAdmin):
    list_display = ['id','tag_name']
    list_display_links = ['id','tag_name']


class MovieAdmin(admin.ModelAdmin):
    list_display = ['id','name','tag','region','star','add_time']
    search_fields = ['name','region','tag']
    list_filter = ['id','name','tag','region','star','add_time']
    list_display_links = ['id','name','tag','region','star','add_time']


class StarAdmin(admin.ModelAdmin):
    list_display = ['id','star']
    list_display_links = ['id','star']


class AddTimeAdmin(admin.ModelAdmin):
    list_display = ['id','add_time']
    list_display_links = ['id','add_time']

admin.site.register(Star,StarAdmin)
admin.site.register(Mov_Tag,Mov_TagAdmin)
admin.site.register(Movie,MovieAdmin)
admin.site.register(AddTime,AddTimeAdmin)
