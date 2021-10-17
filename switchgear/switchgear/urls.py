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
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include

from switchgear import settings
from tracker_app.views import Main, SignUpView, DetailCompanyView, UpdateCompanyView, WorkerDetailView, \
    WorkerUpdateView, SwitchgearListView, SwitchgearDetailView, SwitchgearCreateModelForm, SwitchgearUpdateView, \
    SwitchgearComponentsListView, SwitchgearComponentsCreateView, SwitchgearComponentsUpdateView, \
    SwitchgearComponentsDeleteView, SwitchgearDeleteView, SwitchgearParametersListView, SwitchgearParametersDetailView, \
    SwitchgearParametersUpdateView, SwitchgearParametersDeleteView, ClientListView, ClientCreateView, \
    SwitchgearParametersCreateView, ClientUpdateView, ClientDeleteView, OrderListView, OrderCreateView, OrderDetailView, \
    OrderUpdateView, OrderDeleteView, ComponentListView, ComponentCreateView, ComponentUpdateView, ComponentDeleteView, \
    WorkerPasswordChangeFormView, ClientDetailView

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
    path('worker/edit/password/', WorkerPasswordChangeFormView.as_view(), name='worker_edit_password'),
    path('switchgear/', SwitchgearListView.as_view(), name='switchgear_list'),
    path('switchgear/<int:pk>/', SwitchgearDetailView.as_view(), name='switchgear_detail'),
    path('switchgear/add/', SwitchgearCreateModelForm.as_view(), name='switchgear_add'),
    path('switchgear/edit/<int:pk>/', SwitchgearUpdateView.as_view(), name='switchgear_edit'),
    path('switchgear/delete/<int:pk>/', SwitchgearDeleteView.as_view(), name='switchgear_delete'),
    path('switchgear/components/<int:switchgear_id>/', SwitchgearComponentsListView.as_view(),
         name='switchgear_components_detail'),
    path('switchgear/components/<int:switchgear_id>/add/', SwitchgearComponentsCreateView.as_view(),
         name='switchgear_components_add'),
    path('switchgear/components/edit/<int:pk>/', SwitchgearComponentsUpdateView.as_view(),
         name='switchgear_components_edit'),
    path('switchgear/components/delete/<int:pk>/', SwitchgearComponentsDeleteView.as_view(),
         name='switchgear_components_delete'),
    path('switchgear/parameters/', SwitchgearParametersListView.as_view(), name='switchgear_parameters_list'),
    path('switchgear/parameters/<int:pk>/', SwitchgearParametersDetailView.as_view(),
         name='switchgear_parameters_detail'),
    path('switchgear/parameters/add/', SwitchgearParametersCreateView.as_view(), name='switchgear_parameters_add'),
    path('switchgear/parameters/edit/<int:pk>/', SwitchgearParametersUpdateView.as_view(),
         name='switchgear_parameters_edit'),
    path('switchgear/parameters/delete/<int:pk>/', SwitchgearParametersDeleteView.as_view(),
         name='switchgear_parameters_delete'),
    path('client/', ClientListView.as_view(), name='client_list'),
    path('client/<int:pk>/', ClientDetailView.as_view(), name='client_detail'),
    path('client/add/', ClientCreateView.as_view(), name='client_add'),
    path('client/edit/<int:pk>/', ClientUpdateView.as_view(), name='client_edit'),
    path('client/delete/<int:pk>/', ClientDeleteView.as_view(), name='client_delete'),
    path('order/', OrderListView.as_view(), name='order_list'),
    path('order/add/', OrderCreateView.as_view(), name='order_add'),
    path('order/<int:pk>/', OrderDetailView.as_view(), name='order_detail'),
    path('order/edit/<int:pk>', OrderUpdateView.as_view(), name='order_edit'),
    path('order/delete/<int:pk>/', OrderDeleteView.as_view(), name='order_delete'),
    path('component/', ComponentListView.as_view(), name='component_list'),
    path('component/add/', ComponentCreateView.as_view(), name='component_add'),
    path('component/edit/<int:pk>/', ComponentUpdateView.as_view(), name='component_edit'),
    path('component/delete/<int:pk>/', ComponentDeleteView.as_view(), name='component_delete'),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
