from django.urls import path

from . import views


urlpatterns = [
    path('', views.CatalogListAPIView.as_view(), name='catalog')
]
