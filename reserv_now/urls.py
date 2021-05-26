from django.urls import path, include
from reserv_now import views



urlpatterns = [
    path("", views.reserv_page),
    path("hall_1/", views.hall_one),

]