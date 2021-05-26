from django.urls import path, include
from registration import views



urlpatterns = [
    path("registration/", views.registration, name="registration"),
    path("", views.home_page, name='login'),
    path("log_out",views.log_out, name='logout'),
]