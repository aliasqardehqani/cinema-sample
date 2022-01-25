from django.urls import path
from .views import Signup_view, Login_view, Logout_view

app_name = 'contact'

urlpatterns = [
    path("signup/", Signup_view, name='signup'),
    path("login/", Login_view, name='login'),
    path("logout/", Logout_view, name='logout'),
]

