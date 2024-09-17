from django.urls import path
from . import views

urlpatterns = [
    path('', views.ContactsListAPIView.as_view(), name='contancts')
]
