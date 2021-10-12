from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy

from django.views import View
from django.views.generic import CreateView, DetailView, UpdateView, ListView

from tracker_app.forms import WorkerCreationForm, CompanyModelForm
from tracker_app.models import Company, Worker


class Main(LoginRequiredMixin, View):
    login_url = 'login'

    def get(self, request):
        return render(request, 'home.html')


class SignUpView(CreateView):
    form_class = WorkerCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


class DetailCompanyView(LoginRequiredMixin, DetailView):
    login_url = 'login'
    model = Company
    template_name = 'company.html'


class UpdateCompanyView(PermissionRequiredMixin, UpdateView):
    permission_required = ['tracker_app.change_company']
    model = Company
    form_class = CompanyModelForm
    template_name = 'form.html'
    success_url = '/company/1/'


class WorkerDetailView(LoginRequiredMixin, DetailView):
    login_url = 'login'
    model = Worker
    template_name = 'worker.html'