from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, DetailView, UpdateView, ListView
from django_filters.views import FilterView

from tracker_app.filters import SwitchgearFilter
from tracker_app.forms import WorkerCreationForm, CompanyModelForm, WorkerChangeForm, SwitchgearModelForm
from tracker_app.models import Company, Worker, Switchgear, SwitchgearComponents


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


class WorkerUpdateView(LoginRequiredMixin, UpdateView):
    login_url = 'login'
    model = Worker
    form_class = WorkerChangeForm
    template_name = 'form.html'
    success_url = '/worker/1/'


class SwitchgearListView(LoginRequiredMixin, FilterView):
    login_url = 'login'
    model = Switchgear
    template_name = 'switchgear_list.html'
    ordering = ['serial_no']
    filterset_class = SwitchgearFilter
    paginate_by = 50


class SwitchgearDetailView(LoginRequiredMixin, DetailView):
    login_url = 'login'
    model = Switchgear
    template_name = 'switchgear_detail.html'


class SwitchgearUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = ['tracker_app.change_switchgear']
    model = Switchgear
    form_class = SwitchgearModelForm
    template_name = 'form.html'
    success_url = '/switchgear/'


class SwitchgearCreateModelForm(PermissionRequiredMixin, CreateView):
    permission_required = ['tracker_app.add_switchgear']
    model = Switchgear
    template_name = 'form.html'
    form_class = SwitchgearModelForm
    success_url = '/switchgear/'


class SwitchgearComponentsDetailView(LoginRequiredMixin, ListView):
    login_url = 'login'
    model = SwitchgearComponents
    template_name = 'switchgear_components_detail.html'
    context_object_name = 'switchgear_id'
    paginate_by = 50

    def get_queryset(self):
        return SwitchgearComponents.objects.filter(switchgear_id=self.kwargs['switchgear_id'])


class SwitchgearComponentsUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = ['tracker_app.change_switchgear']
    model = SwitchgearComponents
    form_class = SwitchgearModelForm
    template_name = 'form.html'
    success_url = '/switchgear/'
