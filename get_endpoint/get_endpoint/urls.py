"""get_endpoint URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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

# Endpoint Service URL: 8080

from django.contrib import admin
from django.urls import path
from endpoint import views
from endpoint import one_time_startup

urlpatterns = [
    path('admin/', admin.site.urls),
    path('getDataFromAnalytics/', views.getDataFromAnalytics),
    path('getCBStats/', views.getCBStats)
    #path('getEndpoint/', views.getEndpoint)
]

one_time_startup.one_time_startup()