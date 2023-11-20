from django.urls import path
from user import views

urlpatterns = [
    path('auth', views.authenticate),
]
