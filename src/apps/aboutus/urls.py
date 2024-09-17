from django.urls import path

from . import views

urlpatterns = [
    path('main-page/', views.AboutUsMainPageAPIVIew.as_view(), name='aboutus-main-page'),
    path('', views.AboutUsAPIView.as_view(), name='about-us')
]
