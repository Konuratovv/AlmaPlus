from django.urls import path

from . import views

urlpatterns = [
    path('', views.PartnersListAPIView.as_view(), name='partners')
]
