from django.urls import path

from . import views

urlpatterns = [
    path('', views.EngineeringAPIView.as_view(), name='engineering')
]
