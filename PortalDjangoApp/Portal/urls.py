from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('news/<str:domain>/', views.list_domain, name='list_domain')
]
