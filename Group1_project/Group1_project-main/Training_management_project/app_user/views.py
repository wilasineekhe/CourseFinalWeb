from django.shortcuts import render
from app_user.forms import RegisterForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpRequest, HttpResponseRedirect,HttpResponse
from .forms import UserProfileForm,ExtendProfileForm
from general_APP.models import Course,Enrollment
from django.contrib.auth.models import User
from .models import User_info
from io import BytesIO
import os
from django.conf import settings
from django.views import View
from xhtml2pdf import pisa
from django.template.loader import get_template
from django.contrib.staticfiles import finders


# Create your views here.
def fetch_resources(uri, rel):
        path = os.path.join(settings.MEDIA_ROOT, uri.replace
        (settings.MEDIA_URL, ""))
        return path
def render_to_pdf(template_src, context_dict={}):
	template = get_template(template_src)
	html  = template.render(context_dict)
	result = BytesIO()
	pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result,ink_callback=fetch_resources)
	if not pdf.err:
		return HttpResponse(result.getvalue(), content_type='application/pdf')
	return None

#Opens up page as PDF
class ViewPDF(View):
    def get(self, request:HttpRequest,course_id, *args, **kwargs):
        user = request.user.user_info
        only_course = Course.objects.get(id= course_id)
        data = {
            'userI':user,
            'course':only_course,
        }
        pdf = render_to_pdf('app_user/pdf_template.html',data)
        return HttpResponse(pdf, content_type='application/pdf')
    






@login_required
def User_homepage(request):
    all_obj = Course.objects.all()
    context = {'all_course': all_obj}
    return render(request, 'app_user/user_home.html',context)

@login_required
def User_MyCourse_page(request:HttpRequest):
    user= User_info.objects.filter(id = request.user.user_info.id)[0]
    context = {
        'userI':user,
    }
    return render(request, 'app_user/myCourse_page.html',context)

@login_required
def course_page(request:HttpRequest,course_id):
    only_course = Course.objects.get(id= course_id)
    user = request.user.user_info
    enroll_status = False
    if Enrollment.objects.filter(enroll_course = only_course,enroll_user_info = user).exists():
       enroll = user.enrollment_set.filter(enroll_course = only_course)[0]
       enroll_status = True
    else:
        enroll = ''
        enroll_status = False
        
    context = {
        'only_course': only_course,
        'enroll_status':enroll_status,
        'userI': user,
        'enroll': enroll,
               }
    return render(request,'app_user/course_page.html',context)

@login_required
def enroll_action(request:HttpRequest, course_id):
    course = Course(id = course_id) 
    user = request.user.user_info
    if Enrollment.objects.filter(enroll_course = course,enroll_user_info = user).exists():
        enroll = Enrollment.objects.filter(enroll_course = course,enroll_user_info = user)
        enroll.delete()
    else:
        course = Course(id = course_id) 
        user = request.user.user_info
        enroll = Enrollment()
        enroll.enroll_course = course
        enroll.enroll_user_info = user
        enroll.save()
    return HttpResponseRedirect(reverse('course',args=[str(course_id)],))

@login_required
def user_profile(request:HttpRequest):
    user = request.user
    #POST
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user)
        is_new_profile = False
        try:
            #Will update
            ex_form = ExtendProfileForm(request.POST, instance=user.user_info)
        except:
            #Will create
            ex_form = ExtendProfileForm(request.POST)
            is_new_profile = True
            
        if form.is_valid() and ex_form.is_valid():
            form.save()
            if is_new_profile:
                # Create
                profile:User_info = ex_form.save(commit=False)
                profile.user = user
                profile.username = user.username
                profile.first_name = user.first_name
                profile.last_name = user.last_name
                profile.save()
            else:
                # Update
                ex_form.save()
            
            return HttpResponseRedirect(reverse('profile'))
    else:
        form = UserProfileForm(instance=user)
        try:
            ex_form = ExtendProfileForm(instance=user.user_info)
        except:
            ex_form = ExtendProfileForm()
    #GET
    context = {
        'form' : form,
        'ex_form': ex_form,
        'userI': request.user.user_info
    }
    return render(request,'app_user/profile.html',context)

@login_required
def calender_page(request:HttpRequest):
    course = Course.objects.all()
    context = {'course':course}

    return render(request,'app_user/calender.html',context)

def register(request:HttpRequest):
    user = request.user
    #post
    if request.method == "POST":
        form = RegisterForm(request.POST)
        ex_form = ExtendProfileForm(request.POST)
        if form.is_valid() and ex_form.is_valid():
            user = form.save()
            login(request, user)
            profile:User_info = ex_form.save(commit=False)
            profile.user = user
            profile.username = user.username
            profile.email = user.email
            profile.save()
            return HttpResponseRedirect(reverse('user_homepage'))
    else:
        form = RegisterForm()
        ex_form = ExtendProfileForm()
    #GET
    form = RegisterForm()
    ex_form = ExtendProfileForm()
    context = {
        'form': form,
        'ex_form': ex_form,
               }
    return render(request, 'app_user/register.html', context)
