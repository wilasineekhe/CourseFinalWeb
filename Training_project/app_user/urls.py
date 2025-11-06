from django.urls import path,include
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('', views.User_homepage,name='user_homepage'),
    path('registers', views.register, name='register'),
    path('profile', views.user_profile, name='profile'),
    path('<int:course_id>', views.course_page, name='course'),
    path('<int:course_id>/enroll' , views.enroll_action, name='enroll_button'),
    path('<int:course_id>/pdf_view' , views.ViewPDF.as_view(), name='pdf_button'),
    path('My_course', views.User_MyCourse_page, name='My_course'),
    path('calender', views.calender_page, name='calender'),
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

