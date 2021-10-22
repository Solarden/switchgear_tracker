from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, FormView, ListView
from django_filters.views import FilterView

from tracker_app.filters import SwitchgearFilter, SwitchgearComponentsFilter, SwitchgearParametersFilter, \
    ClientFilter, OrderFilter, ComponentFilter, WorkerFilter
from tracker_app.forms import WorkerCreationForm, CompanyModelForm, WorkerChangeForm, SwitchgearModelForm, \
    SwitchgearComponentsModelForm, SwitchgearParametersModelForm, ClientModelForm, OrderModelForm, ComponentModelForm, \
    WorkerPasswordChangeForm, AdminWorkerChangeForm, SwitchgearPhotosModelForm
from tracker_app.models import Company, Worker, Switchgear, SwitchgearComponents, SwitchgearParameters, Client, Order, \
    Component, SwitchgearPhotos


class Main(LoginRequiredMixin, View):
    login_url = 'login'

    def get(self, request):
        clients = Client.objects.all().count()
        orders = Order.objects.all().count()
        switchgears = Switchgear.objects.all().count()
        try:
            company = Company.objects.get(pk=1)
        except ObjectDoesNotExist:
            company = ''
        return render(request, 'home.html',
                      {'clients': clients, 'orders': orders, 'switchgears': switchgears, 'company': company})


class SignUpView(CreateView):
    form_class = WorkerCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

    def form_invalid(self, form):
        a = super().form_invalid(form)
        return form

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['company'] = Company.objects.get(pk=1)
            return context
        except ObjectDoesNotExist:
            return context


class DetailCompanyView(PermissionRequiredMixin, DetailView):
    permission_required = ['tracker_app.view_company']
    model = Company
    template_name = 'company.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['company'] = Company.objects.get(pk=1)
            return context
        except ObjectDoesNotExist:
            return context


class UpdateCompanyView(PermissionRequiredMixin, UpdateView):
    permission_required = ['tracker_app.change_company']
    model = Company
    form_class = CompanyModelForm
    template_name = 'forms/form.html'
    success_url = '/company/1/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['company'] = Company.objects.get(pk=1)
            return context
        except ObjectDoesNotExist:
            return context


class WorkerListView(PermissionRequiredMixin, FilterView):
    permission_required = ['tracker_app.view_worker']
    model = Worker
    template_name = 'list/worker_list.html'
    filterset_class = WorkerFilter
    paginate_by = 50

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['company'] = Company.objects.get(pk=1)
            return context
        except ObjectDoesNotExist:
            return context


class AdminWorkerDetailView(PermissionRequiredMixin, DetailView):
    permission_required = ['tracker_app.view_worker']
    model = Worker
    template_name = 'detail/admin_worker.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['company'] = Company.objects.get(pk=1)
            return context
        except ObjectDoesNotExist:
            return context


class WorkerDetailView(LoginRequiredMixin, DetailView):
    login_url = 'login'
    model = Worker
    template_name = 'worker.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['company'] = Company.objects.get(pk=1)
            return context
        except ObjectDoesNotExist:
            return context


class WorkerUpdateView(UserPassesTestMixin, UpdateView):
    login_url = 'login'
    model = Worker
    form_class = WorkerChangeForm
    template_name = 'forms/worker_form.html'

    def test_func(self):
        if self.request.user.pk == int(self.kwargs['pk']):
            return True
        else:
            raise Http404

    def get_success_url(self):
        return reverse_lazy('worker_detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['company'] = Company.objects.get(pk=1)
            return context
        except ObjectDoesNotExist:
            return context


class AdminWorkerUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = ['tracker_app.change_worker']
    model = Worker
    form_class = AdminWorkerChangeForm
    template_name = 'forms/admin_worker_form.html'

    def get_success_url(self):
        return reverse_lazy('admin_worker_detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['company'] = Company.objects.get(pk=1)
            return context
        except ObjectDoesNotExist:
            return context


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['company'] = Company.objects.get(pk=1)
            return context
        except ObjectDoesNotExist:
            return context


class SwitchgearListView(PermissionRequiredMixin, FilterView):
    permission_required = ['tracker_app.view_switchgear']
    model = Switchgear
    template_name = 'list/switchgear_list.html'
    ordering = ['serial_no']
    filterset_class = SwitchgearFilter
    paginate_by = 50

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['company'] = Company.objects.get(pk=1)
            return context
        except ObjectDoesNotExist:
            return context


class SwitchgearDetailView(PermissionRequiredMixin, DetailView):
    permission_required = ['tracker_app.view_switchgear']
    model = Switchgear
    template_name = 'detail/switchgear_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['company'] = Company.objects.get(pk=1)
            return context
        except ObjectDoesNotExist:
            return context


class SwitchgearUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = ['tracker_app.change_switchgear']
    model = Switchgear
    form_class = SwitchgearModelForm
    template_name = 'forms/switchgear_form.html'

    def get_success_url(self):
        return reverse_lazy('switchgear_detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['company'] = Company.objects.get(pk=1)
            return context
        except ObjectDoesNotExist:
            return context

    def get_initial(self):
        switchgear = Switchgear.objects.get(pk=self.kwargs['pk'])
        return {
            'has_photos': switchgear.has_photos,
            'stuff_missing': switchgear.stuff_missing,
        }


class SwitchgearCreateModelForm(PermissionRequiredMixin, CreateView):
    permission_required = ['tracker_app.add_switchgear']
    model = Switchgear
    template_name = 'forms/switchgear_form.html'
    form_class = SwitchgearModelForm

    def get_success_url(self):
        return reverse_lazy('switchgear_detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['company'] = Company.objects.get(pk=1)
            return context
        except ObjectDoesNotExist:
            return context


class SwitchgearCreateModelFormPassingOrder(PermissionRequiredMixin, CreateView):
    permission_required = ['tracker_app.add_switchgear']
    model = Switchgear
    template_name = 'forms/switchgear_form.html'
    form_class = SwitchgearModelForm

    def get_success_url(self):
        return reverse_lazy('switchgear_detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['company'] = Company.objects.get(pk=1)
            return context
        except ObjectDoesNotExist:
            return context

    def get_initial(self):
        order = Order.objects.get(pk=self.kwargs['order_id'])
        return {
            'order_ref': order,
        }


class SwitchgearDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = ['tracker_app.delete_switchgear']
    model = Switchgear
    success_url = '/switchgear/'
    template_name = 'delete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['company'] = Company.objects.get(pk=1)
            return context
        except ObjectDoesNotExist:
            return context


class SwitchgearComponentsListView(PermissionRequiredMixin, FilterView):
    permission_required = ['tracker_app.view_switchgearcomponents']
    model = SwitchgearComponents
    template_name = 'list/switchgear_components_list.html'
    context_object_name = 'switchgear_id'
    filterset_class = SwitchgearComponentsFilter
    paginate_by = 50

    def get_queryset(self):
        return SwitchgearComponents.objects.filter(switchgear_id=self.kwargs['switchgear_id'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['main_switchgear'] = Switchgear.objects.filter(pk=self.kwargs['switchgear_id'])
        try:
            context['company'] = Company.objects.get(pk=1)
            return context
        except ObjectDoesNotExist:
            return context


class SwitchgearComponentsCreateView(PermissionRequiredMixin, CreateView):
    permission_required = ['tracker_app.add_switchgearcomponents']
    model = SwitchgearComponents
    template_name = 'forms/form.html'
    form_class = SwitchgearComponentsModelForm

    def get_success_url(self):
        return reverse_lazy('switchgear_components_detail', kwargs={'switchgear_id': self.object.switchgear.pk})

    def get_initial(self):
        switchgear = Switchgear.objects.get(pk=self.kwargs['switchgear_id'])
        return {
            'switchgear': switchgear,
        }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['company'] = Company.objects.get(pk=1)
            return context
        except ObjectDoesNotExist:
            return context

    def form_valid(self, form):
        missing = form.cleaned_data['amount_missing']
        obj = form.cleaned_data['switchgear']
        if missing > 0:
            obj.stuff_missing = True
            obj.save()
        return super().form_valid(form)


class SwitchgearComponentsUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = ['tracker_app.change_switchgearcomponents']
    model = SwitchgearComponents
    form_class = SwitchgearComponentsModelForm
    template_name = 'forms/form.html'

    def get_success_url(self):
        return reverse_lazy('switchgear_components_detail', kwargs={'switchgear_id': self.object.switchgear.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['company'] = Company.objects.get(pk=1)
            return context
        except ObjectDoesNotExist:
            return context

    def form_valid(self, form):
        obj = form.cleaned_data['switchgear']
        check_sum = 0
        check_lst = []
        if form.cleaned_data['amount_missing'] == 0:
            for item in SwitchgearComponents.objects.filter(switchgear=obj):
                check_lst.append(item.amount_missing)
            for x in check_lst:
                if x == 0:
                    check_sum += 1
            if check_sum == len(check_lst) - 1:
                obj.stuff_missing = False
                obj.save()
        else:
            obj.stuff_missing = True
            obj.save()
        return super().form_valid(form)


class SwitchgearComponentsDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = ['tracker_app.delete_switchgearcomponents']
    model = SwitchgearComponents
    success_url = '/switchgear/'
    template_name = 'delete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['company'] = Company.objects.get(pk=1)
            return context
        except ObjectDoesNotExist:
            return context


class SwitchgearParametersCreateView(PermissionRequiredMixin, CreateView):
    permission_required = ['tracker_app.add_switchgearparameters']
    model = SwitchgearParameters
    template_name = 'forms/switchgear_parameters_form.html'
    form_class = SwitchgearParametersModelForm

    def get_success_url(self):
        return reverse_lazy('switchgear_parameters_detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['company'] = Company.objects.get(pk=1)
            return context
        except ObjectDoesNotExist:
            return context


class SwitchgearParametersDetailView(PermissionRequiredMixin, DetailView):
    permission_required = ['tracker_app.view_switchgearparameters']
    model = SwitchgearParameters
    template_name = 'detail/switchgear_parameters_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['company'] = Company.objects.get(pk=1)
            return context
        except ObjectDoesNotExist:
            return context


class SwitchgearParametersUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = ['tracker_app.change_switchgearparameters']
    model = SwitchgearParameters
    template_name = 'forms/switchgear_parameters_form.html'
    form_class = SwitchgearParametersModelForm

    def get_success_url(self):
        return reverse_lazy('switchgear_parameters_detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['company'] = Company.objects.get(pk=1)
            return context
        except ObjectDoesNotExist:
            return context


class SwitchgearParametersDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = ['tracker_app.delete_switchgearparameters']
    model = SwitchgearParameters
    template_name = 'delete.html'
    success_url = '/switchgear/parameters/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['company'] = Company.objects.get(pk=1)
            return context
        except ObjectDoesNotExist:
            return context


class SwitchgearParametersListView(PermissionRequiredMixin, FilterView):
    permission_required = ['tracker_app.view_switchgearparameters']
    model = SwitchgearParameters
    template_name = 'list/switchgear_parameters_list.html'
    filterset_class = SwitchgearParametersFilter
    paginate_by = 50

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['company'] = Company.objects.get(pk=1)
            return context
        except ObjectDoesNotExist:
            return context


class ClientCreateView(PermissionRequiredMixin, CreateView):
    permission_required = ['tracker_app.add_client']
    model = Client
    template_name = 'forms/form.html'
    form_class = ClientModelForm

    def get_success_url(self):
        return reverse_lazy('client_detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['company'] = Company.objects.get(pk=1)
            return context
        except ObjectDoesNotExist:
            return context


class ClientUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = ['tracker_app.change_client']
    model = Client
    template_name = 'forms/form.html'
    form_class = ClientModelForm

    def get_success_url(self):
        return reverse_lazy('client_detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['company'] = Company.objects.get(pk=1)
            return context
        except ObjectDoesNotExist:
            return context


class ClientDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = ['tracker_app.delete_client']
    model = Client
    template_name = 'delete.html'
    success_url = '/client/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['company'] = Company.objects.get(pk=1)
            return context
        except ObjectDoesNotExist:
            return context


class ClientDetailView(PermissionRequiredMixin, DetailView):
    permission_required = ['tracker_app.view_client']
    model = Client
    template_name = 'detail/client_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['orders'] = Order.objects.all().filter(ordered_by=self.object)
        try:
            context['company'] = Company.objects.get(pk=1)
            return context
        except ObjectDoesNotExist:
            return context


class ClientListView(PermissionRequiredMixin, FilterView):
    permission_required = ['tracker_app.view_client']
    model = Client
    template_name = 'list/client_list.html'
    filterset_class = ClientFilter
    paginate_by = 50

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['company'] = Company.objects.get(pk=1)
            return context
        except ObjectDoesNotExist:
            return context


class OrderCreateView(PermissionRequiredMixin, CreateView):
    permission_required = ['tracker_app.add_order']
    model = Order
    template_name = 'forms/form.html'
    form_class = OrderModelForm

    def get_success_url(self):
        return reverse_lazy('order_detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['company'] = Company.objects.get(pk=1)
            return context
        except ObjectDoesNotExist:
            return context

    def get_initial(self):
        return {
            'added_by': self.request.user
        }


class OrderCreateViewPassingClient(PermissionRequiredMixin, CreateView):
    permission_required = ['tracker_app.add_order']
    model = Order
    template_name = 'forms/form.html'
    form_class = OrderModelForm

    def get_success_url(self):
        return reverse_lazy('order_detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['company'] = Company.objects.get(pk=1)
            return context
        except ObjectDoesNotExist:
            return context

    def get_initial(self):
        client = Client.objects.get(pk=self.kwargs['client_id'])
        return {
            'ordered_by': client,
            'added_by': self.request.user
        }


class OrderDetailView(PermissionRequiredMixin, DetailView):
    permission_required = ['tracker_app.view_order']
    login_url = 'login'
    model = Order
    template_name = 'detail/order_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['switchgears'] = Switchgear.objects.all().filter(order_ref=self.object)
        try:
            context['company'] = Company.objects.get(pk=1)
            return context
        except ObjectDoesNotExist:
            return context


class OrderUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = ['tracker_app.change_order']
    model = Order
    template_name = 'forms/form.html'
    form_class = OrderModelForm

    def get_success_url(self):
        return reverse_lazy('order_detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['company'] = Company.objects.get(pk=1)
            return context
        except ObjectDoesNotExist:
            return context


class OrderDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = ['tracker_app.delete_order']
    model = Order
    template_name = 'delete.html'
    success_url = '/order/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['company'] = Company.objects.get(pk=1)
            return context
        except ObjectDoesNotExist:
            return context


class OrderListView(PermissionRequiredMixin, FilterView):
    permission_required = ['tracker_app.view_order']
    model = Order
    template_name = 'list/order_list.html'
    filterset_class = OrderFilter
    paginate_by = 50

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['company'] = Company.objects.get(pk=1)
            return context
        except ObjectDoesNotExist:
            return context


class ComponentCreateView(PermissionRequiredMixin, CreateView):
    permission_required = ['tracker_app.add_component']
    model = Component
    template_name = 'forms/form.html'
    form_class = ComponentModelForm
    success_url = '/component/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['company'] = Company.objects.get(pk=1)
            return context
        except ObjectDoesNotExist:
            return context


class ComponentUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = ['tracker_app.change_component']
    model = Component
    template_name = 'forms/form.html'
    form_class = ComponentModelForm
    success_url = '/component/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['company'] = Company.objects.get(pk=1)
            return context
        except ObjectDoesNotExist:
            return context


class ComponentDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = ['tracker_app.delete_component']
    model = Component
    template_name = 'delete.html'
    success_url = '/component/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['company'] = Company.objects.get(pk=1)
            return context
        except ObjectDoesNotExist:
            return context


class ComponentListView(PermissionRequiredMixin, FilterView):
    permission_required = ['tracker_app.view_component']
    model = Component
    template_name = 'list/component_list.html'
    filterset_class = ComponentFilter
    paginate_by = 50

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['company'] = Company.objects.get(pk=1)
            return context
        except ObjectDoesNotExist:
            return context


class SwitchgearPhotosDetailView(PermissionRequiredMixin, ListView):
    permission_required = ['tracker_app.view_switchgearphotos']
    model = SwitchgearPhotos
    template_name = 'detail/switchgear_photos.html'
    context_object_name = 'switchgear_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['photos'] = SwitchgearPhotos.objects.filter(ref_switchgear=self.kwargs['switchgear_id'])
        context['switchgear'] = Switchgear.objects.get(pk=self.kwargs['switchgear_id'])
        try:
            context['company'] = Company.objects.get(pk=1)
            return context
        except ObjectDoesNotExist:
            return context


class SwitchgearPhotosCreateView(PermissionRequiredMixin, CreateView):
    permission_required = ['tracker_app.add_switchgearphotos']
    model = SwitchgearPhotos
    form_class = SwitchgearPhotosModelForm
    template_name = 'forms/form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['company'] = Company.objects.get(pk=1)
            return context
        except ObjectDoesNotExist:
            return context

    def get_initial(self):
        ref_switchgear = Switchgear.objects.get(pk=self.kwargs['switchgear_id'])
        return {
            'ref_switchgear': ref_switchgear,
        }

    def get_success_url(self):
        return reverse_lazy('switchgear_detail', kwargs={'pk': self.kwargs['switchgear_id']})

    def form_valid(self, form):
        obj = form.cleaned_data['ref_switchgear']
        obj.has_photos = True
        obj.save()
        return super().form_valid(form)


class SwitchgearPhotosDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = ['tracker_app.delete_switchgearphotos']
    model = SwitchgearPhotos
    template_name = 'delete.html'

    def get_success_url(self):
        return reverse_lazy('switchgear_photos', kwargs={'switchgear_id': self.kwargs['switchgear_id']})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['company'] = Company.objects.get(pk=1)
            return context
        except ObjectDoesNotExist:
            return context
