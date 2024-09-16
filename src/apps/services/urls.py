from django.urls import path
from . import views

urlpatterns = [
    path('', views.ServicesListAPIView.as_view(), name='services-list'),
]
