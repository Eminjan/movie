from django.contrib import admin
from .models import UserProfile,Banner
# Register your models here.

class BannerAdmin(admin.ModelAdmin):
    list_display = ['id','title','index','add_time']
    list_filter = ['id','title','index']
    search_fields = ['id','title','index']


class UserPrfileAdmin(admin.ModelAdmin):
    list_display = ['id','username','nick_name','email']
    list_display_links = ['id','username','nick_name','email']


admin.site.register(Banner,BannerAdmin)
admin.site.register(UserProfile,UserPrfileAdmin)