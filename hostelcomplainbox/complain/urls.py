from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from.import  views
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('signup/',views.signup,name='signup'),
    path('home/',views.contact,name='home'),
    path('success/',views.successView,name='success'),
    # path('contactus/',views.contact_us,name='contactus'),
    
    # url(r'^login/',auth_view.LoginView.as_view(template_name='tem/login.html'),name='login'),
    url(r'^$', auth_views.login, {'template_name': 'tem/login.html'}, name='login'),
    url(r'^logout/',auth_views.LogoutView.as_view(template_name='tem/logout.html'),name='logout'),
  ]
