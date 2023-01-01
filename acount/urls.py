from django.contrib import admin
from django.urls import path

from acount import views


urlpatterns = [

    path('login/', views.LoginView.as_view()),
]
