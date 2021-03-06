"""movapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path


from . import views

from users.views import UserInfoView
from movie.views import MovDetailView,MovieWithTagView,MovieWithStarView,MovieWithTimeWith


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('login/',views.login,name='login'),
    path('register/',views.register,name='register'),
    path('logout/',views.logout,name='logout'),
    path('user/',UserInfoView.as_view(),name='user'),
    path('play/<int:movie_id>/',MovDetailView.as_view(),name='play'),
    path('tag/<int:tag_id>/',MovieWithTagView.as_view(),name='movie_with_tag'),
    path('star/<int:star_id>',MovieWithStarView.as_view(),name='movie_with_star'),
    path('time/<int:add_time_id>',MovieWithTimeWith.as_view(),name='movie_with_time'),


]
