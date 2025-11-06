from django.contrib import admin
from .models import Course,Enrollment
from app_user.models import User_info
from django.contrib.auth.models import User
# Register your models here.

class MembershipInline(admin.TabularInline):
    model = Enrollment
    extra = 0
    fields = ['Is_pass','enroll_user_info']
    verbose_name = 'Enrollment'
    
    
class manage_course(admin.ModelAdmin):
    list_display = ['Title', 'Date_open', 'Date_close', 'Is_open', 'Is_full','count_user']
    list_display_links = ['Title', 'Date_open', 'Date_close']
    list_filter = ['Is_open','Is_full']
    search_fields = ['Title__startswith']
    list_editable = ['Is_open', 'Is_full']
    list_per_page = 10
    #fields = ('Title','image' , 'Info','Date_open', 'Date_close', ('Is_open', 'Is_full'))
    fieldsets = (
        (None, {
            "fields": (
                ('Title','code'),
                'lecturer',
                'image',
                'Info',
            ),
        }),
        ('time set',
         {"fields":('Date_open', 'Date_close')
          }),
        ('set status',
         {'classes':('collapse','wide'),
             "fields":('Is_open', 'Is_full'),
             'description': 'Use this fields to manage course status'
          })  
          )
    
    inlines = [
        MembershipInline,
               ]
    #exclude = ["enroll_user_info"]
    def count_user(self,obj:Course):
        count = obj.Enroll_by_user_info.count()
        return f'{count}'
    


admin.site.register(Course, manage_course)