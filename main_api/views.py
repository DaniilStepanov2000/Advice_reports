from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View

from main_api.manager_email import ScheduleManager
from .exceptions import UserExists, IncorrectCredentialsError
import logging
from main_api.manager_process_data import SignUpManager, LoginManager

logger = logging.getLogger('django')

# Create your views here.


def page404(request, exception=None):
    if isinstance(exception, (UserExists, IncorrectCredentialsError)):
        template = "main_api/sign_up.html"
        return render(request, template, {'message': exception.args[0]})

    return HttpResponse('Something is wrong. Try again.')


def page500(request, exception=None):
    return HttpResponse('Internal Server Error')


class LogOutView(View):
    def get(self, request):
        LoginManager(request).logout()
        return redirect('/login/')


class ReportView(View):
    def get(self, request):
        reports = ScheduleManager(request).get_reports()
        return render(request, "main_api/random_word.html", {'reports': reports})

    def post(self, request):
        if 'delete_report_id' in request.POST:
            ScheduleManager(request).delete_schedule()
        elif request.POST['schedule_time']:
            ScheduleManager(request).create_schedule()
        return redirect('/')


class SignUpView(View):
    def get(self, request):
        return render(request, "main_api/sign_up.html")

    def post(self, request):
        SignUpManager(request).create_user()
        return redirect("/login/")


class LoginView(View):
    def get(self, request):
        return render(request, "main_api/login.html", {'message': request.GET.get('message')})

    def post(self, request):
        result = LoginManager(request).login_user()

        if result is True:
            return redirect('/')
        msg = 'Please sign up!'
        return redirect(f'/login/?message={msg}')
