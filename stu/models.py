from django.db import models
from django.db.models.manager import Manager


# Create your models here.
class CustomManager(Manager):
    def getClsObj(self, cname):
        try:
            cls = Clazz.objects.get(cname=cname)
        except Clazz.DoesNotExist:
            cls = Clazz.objects.create(cname=cname)
        return cls

    def getCourseList(self, *coursenames):
        cList = []
        for cn in coursenames:
            try:
                cour = Course.objects.get(course_name=cn)
            except Course.DoesNotExist:
                cour = Course.objects.create(course_name=cn)
            cList.append(cour)
        return cList

    def create(self, **kwargs):
        clazz = kwargs.get('cls', '')
        # 班级信息的入库操作
        clas = self.getClsObj(clazz)
        kwargs['cls'] = clas  # 相当于Student.objects.create(sname='',cls=clas)
        course = kwargs.pop('cour')
        # 学生信息的入库操作
        stu = Manager.create(self, **kwargs)
        # 课程信息的入库操作
        courseList = self.getCourseList(*course)
        # 学生课程的中间表入库操作
        stu.cour.add(*courseList)

    '''
    >>>from stu.models import *
    >>>Student.objects.create(sname='zhaoliu',cls='B999CSS',cour=('css','js'))
    然后数据库中会插入对应的数据
    '''


class Clazz(models.Model):
    cno = models.AutoField(primary_key=True)
    cname = models.CharField(max_length=30)

    def __str__(self):
        return u'Clazz:%s' % self.cname


class Course(models.Model):
    course_no = models.AutoField(primary_key=True)
    course_name = models.CharField(max_length=30)

    def __str__(self):
        return u'Course:%s' % self.course_name


class Student(models.Model):
    sno = models.AutoField(primary_key=True)
    sname = models.CharField(max_length=30)
    cls = models.ForeignKey(Clazz, on_delete=models.CASCADE)
    cour = models.ManyToManyField(Course)

    objects = CustomManager()

    def __str__(self):
        return u'Student:%s' % self.sname


# 完成上一步操作之后输入命令 python manage.py migrate执行迁移文件，数据库中的数据表就创建完成了

# 根据班级名称获取班级对象
def getCls(cname):
    try:
        cls = Clazz.objects.get(cname=cname)
    except Clazz.DoesNotExist:
        cls = Clazz.objects.create(cname=cname)
    return cls


def getCourseList(*coursenames):
    courseList = []
    for cn in coursenames:
        try:
            c = Course.objects.get(course_name=cn)
        except Course.DoesNotExist:
            c = Course.objects.create(course_name=cn)
        courseList.append(c)
    return courseList


def registerStu(sname, cname, *coursenames):
    # 获取班级对象
    cls = getCls(cname)
    # 获取课程对象列表
    courseList = getCourseList(*coursenames)
    # 插入学生表数据
    try:
        stu = Student.objects.get(sname=sname)
    except Student.DoesNotExist:
        stu = Student.objects.create(sname=sname, cls=cls)
    # 插入中间表数据
    stu.cour.add(*courseList)
    return True
