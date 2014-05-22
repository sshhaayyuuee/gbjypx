from django.db import models
from django.forms import ModelForm
from django import forms

# Create your models here.
class Course(models.Model):
    name = models.CharField('班级名称',max_length=50)
    time = models.DateTimeField('开班时间')
    days =  models.IntegerField('学制（天数）',default=0)
    place = models.CharField('地点',max_length=50)
    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField('姓名',max_length = 10)
    genderchoice = ((1, '男'), (0, '女'))
    gender = models.BooleanField('性别', choices = genderchoice,default=1)
    nation = models.CharField('民族', max_length = 6)
    dept = models.CharField('单位', max_length = 20)
    position =  models.CharField('职务', max_length = 20)
    cellphone = models.IntegerField('手机号码',max_length = 11)
    workphone = models.IntegerField('单位电话',null=True,blank=True)
    course = models.ForeignKey(Course)
    def __str__(self):
        return self.name

class StudentForm(ModelForm):
    #def set_course(course_id):

    class Meta:
        model = Student
        fields = ['name',  'gender', 'nation', 'dept', 'position', 'cellphone', 'workphone']

    #def get_absolute_url(self):
    #    return reverse('Student-detail', kwargs={'pk': self.pk})
