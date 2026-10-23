from django.contrib import admin
from CRUD.models import*

class StudentAdmin(admin.ModelAdmin):
	list_display=['name','email','city']

admin.site.register(Student,StudentAdmin)



# Register your models here.
