from django.urls import path
from .views import LoginView, SignUpView, ReportView, LogOutView

urlpatterns = [
    path('', ReportView.as_view(), name='main_url_random_word'),
    path('login/', LoginView.as_view(), name='main_url_random_word_login'),
    path('sign_up/', SignUpView.as_view(), name='main_url_random_word_sign_up'),
    path('logout/', LogOutView.as_view(), name='main_url_random_word_logout'),
]
