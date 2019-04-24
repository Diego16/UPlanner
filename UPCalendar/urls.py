from django.urls import path

from . import views

urlpatterns = [
    path('students', views.StudentsAPI.as_view()),
    path('events', views.EventsAPI.as_view()),
    path('create_event', views.CreateEventAPI.as_view()),
    path("auth/register/", views.RegistrationAPI.as_view()),
    path("auth/login/", views.LoginAPI.as_view()),
    path("auth/user/", views.UserAPI.as_view())

]
