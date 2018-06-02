
from django.shortcuts import render
from django.views.generic.base import View
from .mixin_utils import LoginRequiredMixin
from .models import UserProfile
# Create your views here.


class UserInfoView(LoginRequiredMixin,View):
    """
    用户个人信息
    """
    def get(self,request):
        user = UserProfile.objects.all()
        return render(request,'user.html',{
            'user':user,
        })

