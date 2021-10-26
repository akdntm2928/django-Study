from django.urls import path

from . import views

urlpatterns = [
    path('',views.iasdsadndex, name='index')
]