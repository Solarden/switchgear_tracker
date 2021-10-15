from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.http import Http404
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, FormView
from django_filters.views import FilterView

from tracker_app.filters import SwitchgearFilter, SwitchgearComponentsFilter, SwitchgearParametersFilter, \
    ClientFilter, OrderFilter, ComponentFilter
from tracker_app.forms import WorkerCreationForm, CompanyModelForm, WorkerChangeForm, SwitchgearModelForm, \
    SwitchgearComponentsModelForm, SwitchgearParametersModelForm, ClientModelForm, OrderModelForm, ComponentModelForm, \
    WorkerPasswordChangeForm
from tracker_app.models import Company, Worker, Switchgear, SwitchgearComponents, SwitchgearParameters, Client, Order, \
    Component


class Main(LoginRequiredMixin, View):
    login_url = 'login'

    def get(self, request):
        clients = Client.objects.all().count()
        orders = Order.objects.all().count()
        switchgears = Switchgear.objects.all().count()
        return render(request, 'home.html', {'clients': clients, 'orders': orders, 'switchgears': switchgears})


class SignUpView(CreateView):
    form_class = WorkerCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class DetailCompanyView(PermissionRequiredMixin, DetailView):
    permission_required = ['tracker_app.view_company']
    model = Company
    template_name = 'company.html'


class UpdateCompanyView(PermissionRequiredMixin, UpdateView):
    permission_required = ['tracker_app.change_company']
    model = Company
    form_class = CompanyModelForm
    template_name = 'forms/form.html'
    success_url = '/company/1/'


class WorkerDetailView(LoginRequiredMixin, DetailView):
    login_url = 'login'
    model = Worker
    template_name = 'worker.html'


class WorkerUpdateView(UserPassesTestMixin, UpdateView):
    login_url = 'login'
    model = Worker
    form_class = WorkerChangeForm
    template_name = 'forms/worker_form.html'
    success_url = '/worker/'

    def test_func(self):
        if self.request.user.pk == int(self.kwargs['pk']):
            return True
        else:
            raise Http404


class WorkerPasswordChangeFormView(LoginRequiredMixin, FormView):
    login_url = 'login'
    model = Worker
    form_class = WorkerPasswordChangeForm
    template_name = 'forms/worker_change_password.html'
    success_url = '/'

    def get_form_kwargs(self):
        kwargs = super(WorkerPasswordChangeFormView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        if self.request.method == 'POST':
            kwargs['data'] = self.request.POST
        return kwargs

    def form_valid(self, form):
        form.save()
        update_session_auth_hash(self.request, form.user)
        return super(WorkerPasswordChangeFormView, self).form_valid(form)


class SwitchgearListView(PermissionRequiredMixin, FilterView):
    permission_required = ['tracker_app.view_switchgear']
    model = Switchgear
    template_name = 'list/switchgear_list.html'
    ordering = ['serial_no']
    filterset_class = SwitchgearFilter
    paginate_by = 50


class SwitchgearDetailView(PermissionRequiredMixin, DetailView):
    permission_required = ['tracker_app.view_switchgear']
    model = Switchgear
    template_name = 'detail/switchgear_detail.html'


class SwitchgearUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = ['tracker_app.change_switchgear']
    model = Switchgear
    form_class = SwitchgearModelForm
    template_name = 'forms/switchgear_form.html'
    success_url = '/switchgear/'


class SwitchgearCreateModelForm(PermissionRequiredMixin, CreateView):
    permission_required = ['tracker_app.add_switchgear']
    model = Switchgear
    template_name = 'forms/switchgear_form.html'
    form_class = SwitchgearModelForm
    success_url = '/switchgear/'


class SwitchgearDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = ['tracker_app.delete_switchgear']
    model = Switchgear
    success_url = '/switchgear/'
    template_name = 'delete.html'


class SwitchgearComponentsListView(PermissionRequiredMixin, FilterView):
    permission_required = ['tracker_app.view_switchgearcomponents']
    model = SwitchgearComponents
    template_name = 'list/switchgear_components_list.html'
    context_object_name = 'switchgear_id'
    filterset_class = SwitchgearComponentsFilter
    paginate_by = 50

    def get_queryset(self):
        return SwitchgearComponents.objects.filter(switchgear_id=self.kwargs['switchgear_id'])


class SwitchgearComponentsCreateView(PermissionRequiredMixin, CreateView):
    permission_required = ['tracker_app.add_switchgearcomponents']
    model = SwitchgearComponents
    template_name = 'forms/form.html'
    form_class = SwitchgearComponentsModelForm
    success_url = '/switchgear/'


class SwitchgearComponentsUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = ['tracker_app.change_switchgearcomponents']
    model = SwitchgearComponents
    form_class = SwitchgearComponentsModelForm
    template_name = 'forms/form.html'
    success_url = '/switchgear/'


class SwitchgearComponentsDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = ['tracker_app.delete_switchgearcomponents']
    model = SwitchgearComponents
    success_url = '/switchgear/'
    template_name = 'delete.html'


class SwitchgearParametersCreateView(PermissionRequiredMixin, CreateView):
    permission_required = ['tracker_app.add_switchgearparameters']
    model = SwitchgearParameters
    template_name = 'forms/switchgear_parameters_form.html'
    form_class = SwitchgearParametersModelForm
    success_url = '/switchgear/parameters/'


class SwitchgearParametersDetailView(PermissionRequiredMixin, DetailView):
    permission_required = ['tracker_app.view_switchgearparameters']
    model = SwitchgearParameters
    template_name = 'detail/switchgear_parameters_detail.html'


class SwitchgearParametersUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = ['tracker_app.change_switchgearparameters']
    model = SwitchgearParameters
    template_name = 'forms/switchgear_parameters_form.html'
    form_class = SwitchgearParametersModelForm
    success_url = '/switchgear/parameters/'


class SwitchgearParametersDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = ['tracker_app.delete_switchgearparameters']
    model = SwitchgearParameters
    template_name = 'delete.html'
    success_url = '/switchgear/parameters/'


class SwitchgearParametersListView(PermissionRequiredMixin, FilterView):
    permission_required = ['tracker_app.view_switchgearparameters']
    model = SwitchgearParameters
    template_name = 'list/switchgear_parameters_list.html'
    filterset_class = SwitchgearParametersFilter
    paginate_by = 50


class ClientCreateView(PermissionRequiredMixin, CreateView):
    permission_required = ['tracker_app.add_client']
    model = Client
    template_name = 'forms/form.html'
    form_class = ClientModelForm
    success_url = '/client/'


class ClientUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = ['tracker_app.change_client']
    model = Client
    template_name = 'forms/form.html'
    form_class = ClientModelForm
    success_url = '/client/'


class ClientDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = ['tracker_app.delete_client']
    model = Client
    template_name = 'delete.html'
    success_url = '/client/'


class ClientDetailView(PermissionRequiredMixin, DetailView):
    permission_required = ['tracker_app.view_client']
    model = Client
    template_name = 'detail/client_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['orders'] = Order.objects.all().filter(ordered_by=self.object)
        return context


class ClientListView(PermissionRequiredMixin, FilterView):
    permission_required = ['tracker_app.view_client']
    model = Client
    template_name = 'list/client_list.html'
    filterset_class = ClientFilter
    paginate_by = 50


class OrderCreateView(PermissionRequiredMixin, CreateView):
    permission_required = ['tracker_app.add_order']
    model = Order
    template_name = 'forms/form.html'
    form_class = OrderModelForm
    success_url = '/order/'


class OrderDetailView(PermissionRequiredMixin, DetailView):
    permission_required = ['tracker_app.view_order']
    login_url = 'login'
    model = Order
    template_name = 'detail/order_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['switchgears'] = Switchgear.objects.all().filter(order_ref=self.object)
        return context


class OrderUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = ['tracker_app.change_order']
    model = Order
    template_name = 'forms/form.html'
    form_class = OrderModelForm
    success_url = '/order/'


class OrderDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = ['tracker_app.delete_order']
    model = Order
    template_name = 'delete.html'
    success_url = '/order/'


class OrderListView(PermissionRequiredMixin, FilterView):
    permission_required = ['tracker_app.view_order']
    model = Order
    template_name = 'list/order_list.html'
    filterset_class = OrderFilter
    paginate_by = 50


class ComponentCreateView(PermissionRequiredMixin, CreateView):
    permission_required = ['tracker_app.add_component']
    model = Component
    template_name = 'forms/form.html'
    form_class = ComponentModelForm
    success_url = '/component/'


class ComponentUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = ['tracker_app.change_component']
    model = Component
    template_name = 'forms/form.html'
    form_class = ComponentModelForm
    success_url = '/component/'


class ComponentDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = ['tracker_app.delete_component']
    model = Component
    template_name = 'delete.html'
    success_url = '/component/'


class ComponentListView(PermissionRequiredMixin, FilterView):
    permission_required = ['tracker_app.view_component']
    model = Component
    template_name = 'list/component_list.html'
    filterset_class = ComponentFilter
    paginate_by = 50
