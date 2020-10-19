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


# 显示当前班级下的所有学生信息
def getstu_view(request):
    # 获取班级编号
    cno = request.GET.get('cno', '')
    cno = int(cno)  # 强转，因为数据库中为int类型
    # 根据班级编号查询学生信息
    '''
    python控制台测试用，了解正向还是逆向
    >>>from stu.models import *
    >>>Clazz.objects.get(cno=1)
    >>><Clazz: Clazz:B201python>
    >>>Clazz.objects.get(cno=1).student_set.all()
    >>><QuerySet [<Student: Student:zhangsan>]>
    '''
    stus = Clazz.objects.get(cno=cno).student_set.all()
    return render(request, 'stulist.html', {'stus': stus})
