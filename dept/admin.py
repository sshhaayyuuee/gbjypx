from django.contrib import admin

# Register your models here.
from dept.models import dept

class DeptAdmin(admin.ModelAdmin):
    search_fields = ['name']
	
admin.site.register(dept,DeptAdmin)
