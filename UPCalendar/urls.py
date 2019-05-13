from django.urls import path

from . import views

urlpatterns = [
    path('students/', views.StudentsAPI.as_view()),
    path('events/', views.EventsAPI.as_view()),
    path('create_event/', views.CreateEventAPI.as_view()),
    path('register/', views.RegistrationAPI.as_view()),
    path('login/', views.LoginAPI.as_view()),
    path('user/', views.UserAPI.as_view())

]
