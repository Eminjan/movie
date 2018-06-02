from django.shortcuts import render,get_object_or_404
from django.views.generic.base import View
from .models import Movie,Mov_Tag,Star,AddTime
from django.core.paginator import Paginator


class MovDetailView(View):
    def get(self,request,movie_id):
        movie = Movie.objects.get(id=int(movie_id))
        # 增加播放次数
        movie.play_nums +=1
        movie.save()
        return render(request,'play.html',{
            'movie':movie,
        })


class MovieWithTagView(View):
    def get(self,request,tag_id):
        tag = get_object_or_404(Mov_Tag,id=tag_id)
        movies = Movie.objects.filter(tag=tag)
        tag = tag
        paginator = Paginator(movies, 8)
        page_num = request.GET.get('page', 1)
        page_of_movies = paginator.get_page(page_num)
        current_page_num = page_of_movies.number  # 获取当前页码
        page_range = list(range(max(current_page_num - 2, 1), current_page_num)) + \
                     list(range(current_page_num, min(current_page_num + 2, paginator.num_pages) + 1))
        return render(request,'movies_with_tag.html',{
            'movies':movies,
            'tag':tag,
            'page_of_movies': page_of_movies,
            'page_range': page_range,
    })


class MovieWithStarView(View):
    def get(self,request,star_id):
        star = get_object_or_404(Star,id=star_id)
        movies = Movie.objects.filter(star=star)
        star = star
        paginator = Paginator(movies,8)
        page_num = request.GET.get('page', 1)
        page_of_movies = paginator.get_page(page_num)
        current_page_num = page_of_movies.number  # 获取当前页码
        page_range = list(range(max(current_page_num - 2, 1), current_page_num)) + \
                     list(range(current_page_num, min(current_page_num + 2, paginator.num_pages) + 1))
        return render(request,'movies_with_star.html',{
            'movies':movies,
            'star':star,
            'page_of_movies': page_of_movies,
            'page_range':page_range,
        })


class MovieWithTimeWith(View):
    def get(self,request,add_time_id):
        add_time = get_object_or_404(AddTime,id=add_time_id)
        movies = Movie.objects.filter(add_time=add_time)
        add_time=add_time
        paginator = Paginator(movies, 8)
        page_num = request.GET.get('page', 1)
        page_of_movies = paginator.get_page(page_num)
        current_page_num = page_of_movies.number  # 获取当前页码
        page_range = list(range(max(current_page_num - 2, 1), current_page_num)) + \
                     list(range(current_page_num, min(current_page_num + 2, paginator.num_pages) + 1))
        return render(request,'movies_with_time.html',{
            'movies':movies,
            'add_time':add_time,
            'page_of_movies': page_of_movies,
            'page_range': page_range,
        })