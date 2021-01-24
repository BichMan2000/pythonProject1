from django.urls import path
from . import views

# from django.contrib.auth import views as auth_views
urlpatterns = [

    path('', views.index),
    path('course/', views.course),
    path('login/', views.login),
    path('contact/', views.contact),
    path('register/', views.register),
    path('introduce/', views.introduce),
    path('form_login/', views.form_login),
    # path('login/',auth_views.login, {'template_name':'pages/login.html'})
]
