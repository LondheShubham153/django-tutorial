from django.urls import path

from . import views

urlpatterns = [
    path('',views.index, name="index"),
    path('job',views.job, name="job"),
]