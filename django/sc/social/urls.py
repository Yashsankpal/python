from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

app_name="social"

urlpatterns = [
    path('login',auth_views.LoginView.as_view(template_name='social/login.html'),name='login'),
    path('logout',auth_views.LogoutView.as_view(template_name='thanks.html'),name='logout'),
    path('signup',views.SignUp.as_view(),name='signup')
]
