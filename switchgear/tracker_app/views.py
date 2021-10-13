from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, DetailView, UpdateView, ListView, DeleteView
from django_filters.views import FilterView

from tracker_app.filters import SwitchgearFilter, SwitchgearComponentsFilter
from tracker_app.forms import WorkerCreationForm, CompanyModelForm, WorkerChangeForm, SwitchgearModelForm, \
    SwitchgearComponentsModelForm
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


class SwitchgearDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = ['tracker_app.delete_switchgear']
    model = Switchgear
    success_url = '/switchgear/'
    template_name = 'delete.html'


class SwitchgearComponentsDetailView(LoginRequiredMixin, FilterView):
    login_url = 'login'
    model = SwitchgearComponents
    template_name = 'switchgear_components_list.html'
    context_object_name = 'switchgear_id'
    filterset_class = SwitchgearComponentsFilter
    paginate_by = 50

    def get_queryset(self):
        return SwitchgearComponents.objects.filter(switchgear_id=self.kwargs['switchgear_id'])


class SwitchgearComponentsCreateView(PermissionRequiredMixin, CreateView):
    permission_required = ['tracker_app.add_switchgearcomponents']
    model = SwitchgearComponents
    template_name = 'form.html'
    form_class = SwitchgearComponentsModelForm
    success_url = '/switchgear/'


class SwitchgearComponentsUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = ['tracker_app.change_switchgearcomponents']
    model = SwitchgearComponents
    form_class = SwitchgearComponentsModelForm
    template_name = 'form.html'
    success_url = '/switchgear/'


class SwitchgearComponentsDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = ['tracker_app.delete_switchgearcomponents']
    model = SwitchgearComponents
    success_url = '/switchgear/'
    template_name = 'delete.html'

