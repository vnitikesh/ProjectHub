"""prjcthub URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from projectset import views
from django.conf import settings
from django.conf.urls.static import static
from directory_upload import views as v
from myproject import views as myprojviews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/', views.dashboard, name = 'dashboard'),
    path('podcasts/', views.podcast_view, name = 'podcasts'),
    path('index/', views.my_view, name = 'my-view'),
    path('wohoo/', v.wohoo, name = 'doc'),
    path('myproject/', myprojviews.myproject, name = 'myproject'),
    path('myproject/<str:slug>/', myprojviews.myprojectdetail, name = 'myproject-detail'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
