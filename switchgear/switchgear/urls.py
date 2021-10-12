"""switchgear URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib.auth import views as auth_views

from tracker_app.views import Main, SignUpView, DetailCompanyView, UpdateCompanyView, WorkerDetailView, WorkerUpdateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Main.as_view(), name='home'),
    path('', include('django.contrib.auth.urls')),
    path('login/',
         auth_views.LoginView.as_view(redirect_authenticated_user=True, template_name='registration/login.html'),
         name='login'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('company/<int:pk>/', DetailCompanyView.as_view(), name='company_detail'),
    path('company/edit/<int:pk>/', UpdateCompanyView.as_view(), name='company_edit'),
    path('worker/<int:pk>/', WorkerDetailView.as_view(), name='worker_detail'),
    path('worker/edit/<int:pk>/', WorkerUpdateView.as_view(), name='worker_edit'),
]
