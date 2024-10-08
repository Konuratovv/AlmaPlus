"""
URL configuration for AlmaPlus project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include([
        path('services/', include(('apps.services.urls', 'services'), namespace='services')),
        path('contacts/', include(('apps.contacts.urls', 'contacts'), namespace='contacts')),
        path('catalog/', include(('apps.catalog.urls', 'catalog'), namespace='catalog')),
        path('plast-pipes/', include(('apps.plastpipes.urls', 'plast-pipes'), namespace='plast-pipes')),
        path('partners/', include(('apps.partners.urls', 'partners'), namespace='partners')),
        path('about-us/', include(('apps.aboutus.urls', 'about-us'), namespace='about-us')),
        path('engineering/', include(('apps.engineering.urls', 'engineering'), namespace='engineering')),
    ]))
]
