from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers

from UPCalendar import views

router = routers.DefaultRouter()
router.register('tasks', views.TaskViewSet, 'tasks')
router.register('events', views.EventViewSet, 'events')
router.register('students', views.StudentViewSet, 'students')

urlpatterns = [
    url('^', include(router.urls)),
    path('uevents/', views.UEventsAPI.as_view()),
    path('register/', views.RegistrationAPI.as_view()),
    path('login/', views.LoginAPI.as_view()),
    path('user/', views.UserAPI.as_view())

]
