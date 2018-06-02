#!/usr/bin/python3
# -*-coding:utf-8 -*-
#Author:Eminjan
#@Time  :2018/5/30 17:02

from django.shortcuts import render,redirect,get_object_or_404
from movie.models import Movie,Mov_Tag,Star,AddTime
from users.models import Banner
from django.contrib import auth
from django.contrib.auth.models import User
from django.urls import reverse
from .forms import LoginForm,RegForm
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator


def index(request,):
    movies = Movie.objects.all()
    paginator=Paginator(movies,8) # 每8个进行分页
    page_num = request.GET.get('page', 1)
    page_of_movies = paginator.get_page(page_num)
    current_page_num = page_of_movies.number # 获取当前页码
    page_range =list(range(max(current_page_num -2,1), current_page_num))+\
                list(range(current_page_num, min(current_page_num +2,paginator.num_pages) +1))
    all_banners = Banner.objects.all().order_by('index')
    tags = Mov_Tag.objects.all()[:5]
    stars = Star.objects.all()

    add_times = AddTime.objects.all()[:5]
    return render(request,'index.html',{
        'all_banners': all_banners,
        'tags':tags,
        'page_of_movies': page_of_movies,
        'stars':stars,
        'add_times':add_times,
        'page_range':page_range,
    })


def login(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user = login_form.cleaned_data['user']
            auth.login(request, user)
            return redirect(request.GET.get('from', reverse('index')))
    else:
        login_form = LoginForm()

    context = {}
    context['login_form'] = login_form
    return render(request, 'login.html', context)


def register(request):
    if request.method == 'POST':
        reg_form = RegForm(request.POST)
        if reg_form.is_valid():
            username = reg_form.cleaned_data['username']
            email = reg_form.cleaned_data['email']
            password = reg_form.cleaned_data['password']
            # 创建用户
            user = User.objects.create_user(username, email, password)
            user.save()
            # 登录用户
            user = auth.authenticate(username=username, password=password)
            auth.login(request, user)
            return redirect(request.GET.get('from', reverse('index')))
    else:
        reg_form = RegForm()
    context = {}
    context['reg_form'] = reg_form
    return render(request, 'register.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))







