from django.contrib import admin

from app.models import Students

# Register your models here.
class StudensModel(admin.ModelAdmin):
    list_display=['id','username','first_name','last_name','email','mobile_number','profilepic']

admin.site.register(Students,StudensModel)