from django.contrib import admin
# Register your models here.

from enrollment.models import Student,Course

class StudentAdmin(admin.ModelAdmin):
    list_display = ('name','gender','dept','course')
    list_filter = ['course']
    search_fields = ['name']

class CourseAdmin(admin.ModelAdmin):
    list_display = ('name','time','days','place')
    search_fields = ['name','days']
	
admin.site.register(Student,StudentAdmin)
admin.site.register(Course,CourseAdmin)
