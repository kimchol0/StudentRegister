from django.db import models


# Create your models here.
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
    cls = models.ForeignKey(Clazz,on_delete=models.CASCADE)
    cour = models.ManyToManyField(Course)

    def __str__(self):
        return u'Student:%s' % self.sname
