from django.urls import path

from . import views

urlpatterns = [
    path('', views.PlastPipesCategoryListAPIView.as_view(), name='plastic-pipes'),
]
