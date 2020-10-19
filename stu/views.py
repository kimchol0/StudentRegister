from django.http import HttpResponse
from django.shortcuts import render
from .models import *


# Create your views here.
def index_view(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    else:
        # 接收请求参数
        sname = request.POST.get('sname', '')
        cname = request.POST.get('clsname', '')
        coursenames = request.POST.getlist('coursename', [])
        # 将数据注册到数据库
        flag = registerStu(sname, cname, *coursenames)
        if flag:
            return HttpResponse('注册成功！')
        return HttpResponse('注册失败！')


# 显示所有班级信息
def showall_view(request):
    # 查询班级表中的所有数据
    cls = Clazz.objects.all()
    return render(request, 'showall.html', {'cls': cls})
