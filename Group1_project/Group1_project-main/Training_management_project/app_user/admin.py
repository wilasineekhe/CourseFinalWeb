from django.contrib import admin
from app_user.models import User_info
from django.contrib.auth.models import User
from general_APP.models import Course,Enrollment
# Register your models here.
class MembershipInline(admin.TabularInline):
    model = Enrollment
    extra = 0
    fields = ['Is_pass','enroll_course']
    verbose_name = 'Enrollment'
    empty_value_display = "-empty-"
    def set_name(self,obj):
        pass
class manage_User_info(admin.ModelAdmin):
    list_display = ['student_ID','first_name', 'last_name','username', 'email']
    list_display_links = ['student_ID','first_name', 'last_name','username', 'email']
    list_filter = ['student_ID','first_name']
    search_fields = ['first_name']
    fields = ('username',('first_name' , 'last_name'),'student_ID', 'email')
    list_per_page = 10
    inlines = [
        MembershipInline,
               ]
    #exclude = ["enroll_user_info"]


admin.site.register(User_info, manage_User_info)