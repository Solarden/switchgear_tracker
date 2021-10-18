import pytest
from django.core.exceptions import ObjectDoesNotExist
from django.test import Client
from django.urls import reverse

from tracker_app.models import Worker
from .models import Client as ModelClient, Company, Order, SwitchgearParameters, Switchgear, Component, \
    SwitchgearComponents


# LOGIN/SIGNUP VIEWS TESTS

def test_login():
    client = Client()
    response = client.get(reverse("login"))
    assert response.status_code == 200


@pytest.mark.django_db
def test_login_with_login(user):
    client = Client()
    client.force_login(user)
    response = client.get(reverse('login'))
    assert response.status_code == 200


@pytest.mark.django_db
def test_signup(user):
    client = Client()
    client.force_login(user)
    response = client.get(reverse("signup"))
    assert response.status_code == 200


@pytest.mark.django_db
def test_signup_post_register():
    client = Client()
    a = {
        'username': 'zajączek',
        'email': 'test@test.pl',
        'first_name': 'pawel',
        'last_name': 'testowy',
        'password1': 'tymczasowe!@#',
        'password2': 'tymczasowe!@#',
    }
    response = client.post(reverse("signup"), data=a)
    assert response.status_code == 302
    del a['password1']
    del a['password2']
    Worker.objects.get(**a)


@pytest.mark.django_db
def test_login_post(user):
    client = Client()
    a = {
        'username': 'zajączek',
        'email': 'test@test.pl',
        'first_name': 'pawel',
        'last_name': 'testowy',
        'password1': 'tymczasowe!@#',
        'password2': 'tymczasowe!@#',
    }
    response = client.post(reverse("signup"), data=a)
    assert response.status_code == 302
    b = {
        'username': 'zajączek',
        'password': 'tymczasowe!@#',
    }
    response = client.post(reverse("login"), data=b)
    assert response.status_code == 302


# WORKER VIEW TESTS

@pytest.mark.django_db
def test_worker_detail_no_login(user):
    client = Client()
    response = client.get(reverse('worker_detail', kwargs={'pk': user.pk}))
    assert response.status_code == 302


@pytest.mark.django_db
def test_worker_detail_r_logged_in(user):
    client = Client()
    client.force_login(user)
    response = client.get(reverse('worker_detail', kwargs={'pk': user.pk}))
    assert response.status_code == 200


@pytest.mark.django_db
def test_worker_u_no_login(user):
    client = Client()
    response = client.get(reverse('worker_edit', kwargs={'pk': user.pk}))
    assert response.status_code == 404


@pytest.mark.django_db
def test_worker_u_with_login_get(user):
    client = Client()
    client.force_login(user)
    response = client.get(reverse('worker_edit', kwargs={'pk': user.pk}))
    assert response.status_code == 200


@pytest.mark.django_db
def test_worker_u_with_login_post(user):
    client = Client()
    client.force_login(user)
    a = {
        'username': 'line100',
        'email': 'test@test.pl',
        'first_name': 'janek',
        'last_name': 'testowy',
    }
    response = client.post(reverse('worker_edit', kwargs={'pk': user.pk}), data=a)
    assert response.status_code == 302


# HOME VIEW TESTS

def test_home_no_login():
    client = Client()
    response = client.get(reverse('home'))
    assert response.status_code == 302


@pytest.mark.django_db
def test_home_with_login(user):
    client = Client()
    client.force_login(user)
    response = client.get(reverse('home'))
    assert response.status_code == 200


# CLIENT VIEWS TESTS

def test_client_list_no_login():
    client = Client()
    response = client.get(reverse('client_list'))
    assert response.status_code == 302


@pytest.mark.django_db
def test_client_c_no_perm(user):
    client = Client()
    client.force_login(user)
    response = client.get(reverse('client_add'))
    assert response.status_code == 403


@pytest.mark.django_db
def test_client_c_with_perm_get(user_perm_c_client):
    client = Client()
    client.force_login(user_perm_c_client)
    response = client.get(reverse('client_add'))
    assert response.status_code == 200


@pytest.mark.django_db
def test_client_c_with_perm_post(user_perm_c_client):
    client = Client()
    client.force_login(user_perm_c_client)
    a = {
        'name': 'line 90'
    }
    response = client.post(reverse('client_add'), data=a)
    assert response.status_code == 302
    ModelClient.objects.get(**a)


@pytest.mark.django_db
def test_client_list_r_no_perm(user):
    client = Client()
    client.force_login(user)
    response = client.get(reverse('client_list'))
    assert response.status_code == 403


@pytest.mark.django_db
def test_client_list_r_with_perm_get(user_perm_cr_client):
    client = Client()
    client.force_login(user_perm_cr_client)
    response = client.get(reverse('client_list'))
    assert response.status_code == 200


@pytest.mark.django_db
def test_client_list_r_get_not_empty(clients, user_perm_cr_client):
    client = Client()
    client.force_login(user_perm_cr_client)
    response = client.get(reverse("client_list"))
    assert response.status_code == 200
    client_list = response.context['object_list']
    assert client_list.count() == len(clients)
    for client in clients:
        assert client in client_list


@pytest.mark.django_db
def test_client_detail_r_no_perm(user, add_client):
    client = Client()
    client.force_login(user)
    response = client.get(reverse('client_detail', kwargs={'pk': add_client.pk}))
    assert response.status_code == 403


@pytest.mark.django_db
def test_client_detail_r_with_perm(user_perm_cr_client, add_client):
    client = Client()
    client.force_login(user_perm_cr_client)
    response = client.get(reverse('client_detail', kwargs={'pk': add_client.pk}))
    assert response.status_code == 200


@pytest.mark.django_db
def test_client_detail_u_no_perm(user_perm_cr_client, add_client):
    client = Client()
    client.force_login(user_perm_cr_client)
    response = client.get(reverse('client_edit', kwargs={'pk': add_client.pk}))
    assert response.status_code == 403


@pytest.mark.django_db
def test_client_detail_u_with_perm_get(user_perm_cru_client, add_client):
    client = Client()
    client.force_login(user_perm_cru_client)
    response = client.get(reverse('client_edit', kwargs={'pk': add_client.pk}))
    assert response.status_code == 200


@pytest.mark.django_db
def test_client_detail_u_with_perm_post(user_perm_cru_client, add_client):
    client = Client()
    client.force_login(user_perm_cru_client)
    a = {
        'name': 'test line 100'
    }
    response = client.post(reverse('client_edit', kwargs={'pk': add_client.pk}), data=a)
    assert response.status_code == 302


@pytest.mark.django_db
def test_client_detail_d_no_perm(user_perm_cr_client, add_client):
    client = Client()
    client.force_login(user_perm_cr_client)
    response = client.get(reverse('client_delete', kwargs={'pk': add_client.pk}))
    assert response.status_code == 403


@pytest.mark.django_db
def test_client_detail_d_with_perm_get(user_perm_crud_client, add_client):
    client = Client()
    client.force_login(user_perm_crud_client)
    response = client.get(reverse('client_delete', kwargs={'pk': add_client.pk}))
    assert response.status_code == 200


@pytest.mark.django_db
def test_client_detail_d_with_perm_post(user_perm_crud_client, add_client):
    client = Client()
    client.force_login(user_perm_crud_client)
    response = client.post(reverse('client_delete', kwargs={'pk': add_client.pk}))
    assert response.status_code == 302
    with pytest.raises(ObjectDoesNotExist):
        ModelClient.objects.get(pk=add_client.pk)


# COMPANY VIEWS TESTS

def test_company_list_no_login():
    client = Client()
    response = client.get(reverse('component_list'))
    assert response.status_code == 302


@pytest.mark.django_db
def test_company_r_no_perm(user, add_company):
    client = Client()
    client.force_login(user)
    response = client.get(reverse('company_detail', kwargs={'pk': add_company.pk}))
    assert response.status_code == 403


@pytest.mark.django_db
def test_company_r_with_perm(user_perm_cr_company, add_company):
    client = Client()
    client.force_login(user_perm_cr_company)
    response = client.get(reverse('company_detail', kwargs={'pk': add_company.pk}))
    assert response.status_code == 200


@pytest.mark.django_db
def test_company_u_no_perm(user_perm_cr_company, add_company):
    client = Client()
    client.force_login(user_perm_cr_company)
    response = client.get(reverse('company_edit', kwargs={'pk': add_company.pk}))
    assert response.status_code == 403


@pytest.mark.django_db
def test_company_u_with_perm_get(user_perm_cru_company, add_company):
    client = Client()
    client.force_login(user_perm_cru_company)
    response = client.get(reverse('company_edit', kwargs={'pk': add_company.pk}))
    assert response.status_code == 200


@pytest.mark.django_db
def test_company_u_with_perm_post(user_perm_cru_company, add_company):
    client = Client()
    client.force_login(user_perm_cru_company)
    a = {
        'name': 'test', 'owner': 'test', 'nip': 'test', 'hq': 'test', 'prod': 'test', 'logo': 'test'
    }
    response = client.post(reverse('company_edit', kwargs={'pk': add_company.pk}), data=a)
    assert response.status_code == 302
    Company.objects.get(name='test')


# Order VIEWS TESTS

def test_order_list_no_login():
    client = Client()
    response = client.get(reverse('order_list'))
    assert response.status_code == 302


@pytest.mark.django_db
def test_order_c_no_perm(user):
    client = Client()
    client.force_login(user)
    response = client.get(reverse('order_add'))
    assert response.status_code == 403


@pytest.mark.django_db
def test_order_c_with_perm_get(user_perm_c_order):
    client = Client()
    client.force_login(user_perm_c_order)
    response = client.get(reverse('order_add'))
    assert response.status_code == 200


@pytest.mark.django_db
def test_order_c_with_perm_post(user_perm_c_order, add_client):
    client = Client()
    client.force_login(user_perm_c_order)
    a = {
        'order_name': 'x', 'ordered_by': add_client.pk, 'added_by': user_perm_c_order.pk
    }
    response = client.post(reverse('order_add'), data=a)
    assert response.status_code == 302
    Order.objects.get(**a)


@pytest.mark.django_db
def test_order_list_r_no_perm(user_perm_c_order, add_order):
    client = Client()
    client.force_login(user_perm_c_order)
    response = client.get(reverse('order_list'))
    assert response.status_code == 403


@pytest.mark.django_db
def test_order_list_r_with_perm(user_perm_cr_order, add_order):
    client = Client()
    client.force_login(user_perm_cr_order)
    response = client.get(reverse('order_list'))
    assert response.status_code == 200


@pytest.mark.django_db
def test_client_list_get_not_empty(orders, user_perm_cr_order):
    client = Client()
    client.force_login(user_perm_cr_order)
    response = client.get(reverse("order_list"))
    assert response.status_code == 200
    client_list = response.context['object_list']
    assert client_list.count() == len(orders)
    for client in orders:
        assert client in client_list


@pytest.mark.django_db
def test_order_detail_r_no_perm(user_perm_c_order, add_order):
    client = Client()
    client.force_login(user_perm_c_order)
    response = client.get(reverse('order_detail', kwargs={'pk': add_order.pk}))
    assert response.status_code == 403


@pytest.mark.django_db
def test_order_detail_r_with_perm(user_perm_cr_order, add_order):
    client = Client()
    client.force_login(user_perm_cr_order)
    response = client.get(reverse('order_detail', kwargs={'pk': add_order.pk}))
    assert response.status_code == 200


@pytest.mark.django_db
def test_order_u_no_perm(user_perm_cr_order, add_order):
    client = Client()
    client.force_login(user_perm_cr_order)
    response = client.get(reverse('order_edit', kwargs={'pk': add_order.pk}))
    assert response.status_code == 403


@pytest.mark.django_db
def test_order_u_with_perm_get(user_perm_cru_order, add_order):
    client = Client()
    client.force_login(user_perm_cru_order)
    response = client.get(reverse('order_edit', kwargs={'pk': add_order.pk}))
    assert response.status_code == 200


@pytest.mark.django_db
def test_order_u_with_perm_post(user_perm_cru_order, add_order, add_client):
    client = Client()
    client.force_login(user_perm_cru_order)
    a = {
        'order_name': 'test',
        'ordered_by': add_client.pk,
        'added_by': user_perm_cru_order.pk,
    }
    response = client.post(reverse('order_edit', kwargs={'pk': add_order.pk}), data=a)
    assert response.status_code == 302
    Order.objects.get(**a)


@pytest.mark.django_db
def test_order_d_no_perm(user_perm_cru_order, add_order):
    client = Client()
    client.force_login(user_perm_cru_order)
    response = client.get(reverse('order_delete', kwargs={'pk': add_order.pk}))
    assert response.status_code == 403


@pytest.mark.django_db
def test_order_d_with_perm_get(user_perm_crud_order, add_order):
    client = Client()
    client.force_login(user_perm_crud_order)
    response = client.get(reverse('order_delete', kwargs={'pk': add_order.pk}))
    assert response.status_code == 200


@pytest.mark.django_db
def test_order_d_with_perm_post(user_perm_crud_order, add_order):
    client = Client()
    client.force_login(user_perm_crud_order)
    response = client.post(reverse('order_delete', kwargs={'pk': add_order.pk}))
    assert response.status_code == 302
    with pytest.raises(ObjectDoesNotExist):
        Order.objects.get(pk=add_order.pk)


# SwitchgearParameters VIEWS TESTS

def test_switchgearparameters_list_no_login():
    client = Client()
    response = client.get(reverse('switchgear_parameters_list'))
    assert response.status_code == 302


@pytest.mark.django_db
def test_switchgearparameters_c_no_perm(user):
    client = Client()
    client.force_login(user)
    response = client.get(reverse('switchgear_parameters_add'))
    assert response.status_code == 403


@pytest.mark.django_db
def test_switchgearparameters_c_with_perm_get(user_perm_c_switchgearparameters):
    client = Client()
    client.force_login(user_perm_c_switchgearparameters)
    response = client.get(reverse('switchgear_parameters_add'))
    assert response.status_code == 200


@pytest.mark.django_db
def test_switchgearparameters_c_with_perm_post(user_perm_c_switchgearparameters):
    client = Client()
    client.force_login(user_perm_c_switchgearparameters)
    x = '1'
    a = {
        'name': x, 'par_a': x, 'par_ka': x, 'par_v': x, 'par_ui': x, 'par_hz': x, 'par_grid': x,
        'par_protection': x, 'par_ip': x, 'par_ik': x
    }
    response = client.post(reverse('switchgear_parameters_add'), data=a)
    assert response.status_code == 302
    SwitchgearParameters.objects.get(**a)


@pytest.mark.django_db
def test_switchgearparameters_list_r_no_perm(user_perm_c_switchgearparameters):
    client = Client()
    client.force_login(user_perm_c_switchgearparameters)
    response = client.get(reverse('switchgear_parameters_list'))
    assert response.status_code == 403


@pytest.mark.django_db
def test_switchgearparameters_list_r_with_perm(user_perm_cr_switchgearparameters):
    client = Client()
    client.force_login(user_perm_cr_switchgearparameters)
    response = client.get(reverse('switchgear_parameters_list'))
    assert response.status_code == 200


@pytest.mark.django_db
def test_switchgearparameters_list_get_not_empty(switchgearparameters, user_perm_cr_switchgearparameters):
    client = Client()
    client.force_login(user_perm_cr_switchgearparameters)
    response = client.get(reverse("switchgear_parameters_list"))
    assert response.status_code == 200
    object_list = response.context['object_list']
    assert object_list.count() == len(switchgearparameters)
    for item in switchgearparameters:
        assert item in object_list


@pytest.mark.django_db
def test_switchgearparameters_detail_r_no_perm(user_perm_c_switchgearparameters, add_switchgearparameters):
    client = Client()
    client.force_login(user_perm_c_switchgearparameters)
    response = client.get(reverse('switchgear_parameters_detail', kwargs={'pk': add_switchgearparameters.pk}))
    assert response.status_code == 403


@pytest.mark.django_db
def test_switchgearparameters_detail_r_with_perm(user_perm_cr_switchgearparameters, add_switchgearparameters):
    client = Client()
    client.force_login(user_perm_cr_switchgearparameters)
    response = client.get(reverse('switchgear_parameters_detail', kwargs={'pk': add_switchgearparameters.pk}))
    assert response.status_code == 200


@pytest.mark.django_db
def test_switchgearparameters_u_no_perm(user_perm_c_switchgearparameters, add_switchgearparameters):
    client = Client()
    client.force_login(user_perm_c_switchgearparameters)
    response = client.get(reverse('switchgear_parameters_edit', kwargs={'pk': add_switchgearparameters.pk}))
    assert response.status_code == 403


@pytest.mark.django_db
def test_switchgearparameters_u_with_perm_get(user_perm_cru_switchgearparameters, add_switchgearparameters):
    client = Client()
    client.force_login(user_perm_cru_switchgearparameters)
    response = client.get(reverse('switchgear_parameters_edit', kwargs={'pk': add_switchgearparameters.pk}))
    assert response.status_code == 200


@pytest.mark.django_db
def test_switchgearparameters_u_with_perm_post(user_perm_cru_switchgearparameters, add_switchgearparameters):
    client = Client()
    client.force_login(user_perm_cru_switchgearparameters)
    x = '2137'
    a = {
        'name': x, 'par_a': x, 'par_ka': x, 'par_v': x, 'par_ui': x, 'par_hz': x, 'par_grid': x,
        'par_protection': x, 'par_ip': x, 'par_ik': x
    }
    response = client.post(reverse('switchgear_parameters_edit', kwargs={'pk': add_switchgearparameters.pk}), data=a)
    assert response.status_code == 302
    SwitchgearParameters.objects.get(**a)


@pytest.mark.django_db
def test_switchgearparameters_d_no_perm(user_perm_c_switchgearparameters, add_switchgearparameters):
    client = Client()
    client.force_login(user_perm_c_switchgearparameters)
    response = client.get(reverse('switchgear_parameters_delete', kwargs={'pk': add_switchgearparameters.pk}))
    assert response.status_code == 403


@pytest.mark.django_db
def test_switchgearparameters_d_with_perm_get(user_perm_crud_switchgearparameters, add_switchgearparameters):
    client = Client()
    client.force_login(user_perm_crud_switchgearparameters)
    response = client.get(reverse('switchgear_parameters_delete', kwargs={'pk': add_switchgearparameters.pk}))
    assert response.status_code == 200


@pytest.mark.django_db
def test_switchgearparameters_d_with_perm_post(user_perm_crud_switchgearparameters, add_switchgearparameters):
    client = Client()
    client.force_login(user_perm_crud_switchgearparameters)
    response = client.post(reverse('switchgear_parameters_delete', kwargs={'pk': add_switchgearparameters.pk}))
    assert response.status_code == 302
    with pytest.raises(ObjectDoesNotExist):
        Order.objects.get(pk=add_switchgearparameters.pk)


# Switchgear VIEWS TESTS

def test_switchgear_list_no_login():
    client = Client()
    response = client.get(reverse('switchgear_list'))
    assert response.status_code == 302


@pytest.mark.django_db
def test_switchgear_no_perm(user):
    client = Client()
    client.force_login(user)
    response = client.get(reverse('switchgear_add'))
    assert response.status_code == 403


@pytest.mark.django_db
def test_switchgear_c_with_perm_get(user_perm_c_switchgear):
    client = Client()
    client.force_login(user_perm_c_switchgear)
    response = client.get(reverse('switchgear_add'))
    assert response.status_code == 200


@pytest.mark.django_db
def test_switchgear_c_with_perm_post(user_perm_c_switchgear, add_order, add_switchgearparameters):
    client = Client()
    client.force_login(user_perm_c_switchgear)
    x = '1'
    a = {
        'order_ref': add_order.pk, 'name': x, 'serial_no': x,
        'switchgear_parameters': add_switchgearparameters.pk, 'made_by': user_perm_c_switchgear.pk
    }
    response = client.post(reverse('switchgear_add'), data=a)
    assert response.status_code == 302
    Switchgear.objects.get(**a)


@pytest.mark.django_db
def test_switchgear_list_r_no_perm(user_perm_c_switchgear):
    client = Client()
    client.force_login(user_perm_c_switchgear)
    response = client.get(reverse('switchgear_list'))
    assert response.status_code == 403


@pytest.mark.django_db
def test_switchgear_list_r_with_perm(user_perm_cr_switchgear):
    client = Client()
    client.force_login(user_perm_cr_switchgear)
    response = client.get(reverse('switchgear_add'))
    assert response.status_code == 200


@pytest.mark.django_db
def test_switchgear_list_get_not_empty(switchgears, user_perm_cr_switchgear):
    client = Client()
    client.force_login(user_perm_cr_switchgear)
    response = client.get(reverse("switchgear_list"))
    assert response.status_code == 200
    object_list = response.context['object_list']
    assert object_list.count() == len(switchgears)
    for item in switchgears:
        assert item in object_list


@pytest.mark.django_db
def test_switchgear_detail_r_no_perm(user_perm_c_switchgear, add_switchgear):
    client = Client()
    client.force_login(user_perm_c_switchgear)
    response = client.get(reverse('switchgear_detail', kwargs={'pk': add_switchgear.pk}))
    assert response.status_code == 403


@pytest.mark.django_db
def test_switchgear_detail_r_with_perm(user_perm_cr_switchgear, add_switchgear):
    client = Client()
    client.force_login(user_perm_cr_switchgear)
    response = client.get(reverse('switchgear_detail', kwargs={'pk': add_switchgear.pk}))
    assert response.status_code == 200


@pytest.mark.django_db
def test_switchgear_u_no_perm_get(user_perm_c_switchgear, add_switchgear):
    client = Client()
    client.force_login(user_perm_c_switchgear)
    response = client.get(reverse('switchgear_edit', kwargs={'pk': add_switchgear.pk}))
    assert response.status_code == 403


@pytest.mark.django_db
def test_switchgear_u_with_perm_get(user_perm_cru_switchgear, add_switchgear):
    client = Client()
    client.force_login(user_perm_cru_switchgear)
    response = client.get(reverse('switchgear_edit', kwargs={'pk': add_switchgear.pk}))
    assert response.status_code == 200


@pytest.mark.django_db
def test_switchgear_u_with_perm_post(user_perm_cru_switchgear, add_switchgear, add_order, add_switchgearparameters):
    client = Client()
    client.force_login(user_perm_cru_switchgear)
    x = 'test2137'
    a = {
        'order_ref': add_order.pk, 'name': x, 'serial_no': x,
        'switchgear_parameters': add_switchgearparameters.pk, 'made_by': user_perm_cru_switchgear.pk
    }
    response = client.post(reverse('switchgear_edit', kwargs={'pk': add_switchgear.pk}), data=a)
    assert response.status_code == 302
    Switchgear.objects.get(**a)


@pytest.mark.django_db
def test_switchgear_d_no_perm_get(user_perm_c_switchgear, add_switchgear):
    client = Client()
    client.force_login(user_perm_c_switchgear)
    response = client.get(reverse('switchgear_delete', kwargs={'pk': add_switchgear.pk}))
    assert response.status_code == 403


@pytest.mark.django_db
def test_switchgear_d_with_perm_get(user_perm_crud_switchgear, add_switchgear):
    client = Client()
    client.force_login(user_perm_crud_switchgear)
    response = client.get(reverse('switchgear_delete', kwargs={'pk': add_switchgear.pk}))
    assert response.status_code == 200


@pytest.mark.django_db
def test_switchgear_d_with_perm_post(user_perm_crud_switchgear, add_switchgear):
    client = Client()
    client.force_login(user_perm_crud_switchgear)
    response = client.post(reverse('switchgear_delete', kwargs={'pk': add_switchgear.pk}))
    assert response.status_code == 302
    with pytest.raises(ObjectDoesNotExist):
        Switchgear.objects.get(pk=add_switchgear.pk)


# Component VIEWS TESTS

def test_component_list_no_login():
    client = Client()
    response = client.get(reverse('component_list'))
    assert response.status_code == 302


@pytest.mark.django_db
def test_component_no_perm(user):
    client = Client()
    client.force_login(user)
    response = client.get(reverse('component_add'))
    assert response.status_code == 403


@pytest.mark.django_db
def test_component_c_with_perm_get(user_perm_c_component):
    client = Client()
    client.force_login(user_perm_c_component)
    response = client.get(reverse('component_add'))
    assert response.status_code == 200


@pytest.mark.django_db
def test_component_c_with_perm_post(user_perm_c_component):
    client = Client()
    client.force_login(user_perm_c_component)
    x = 'siema'
    a = {
        'name': x, 'producer': x, 'catalogue_number': x
    }
    response = client.post(reverse('component_add'), data=a)
    assert response.status_code == 302
    Component.objects.get(**a)


@pytest.mark.django_db
def test_component_list_r_no_perm(user_perm_c_component):
    client = Client()
    client.force_login(user_perm_c_component)
    response = client.get(reverse('component_list'))
    assert response.status_code == 403


@pytest.mark.django_db
def test_component_list_r_with_perm_get(user_perm_cr_component):
    client = Client()
    client.force_login(user_perm_cr_component)
    response = client.get(reverse('component_list'))
    assert response.status_code == 200


@pytest.mark.django_db
def test_component_list_get_not_empty(components, user_perm_cr_component):
    client = Client()
    client.force_login(user_perm_cr_component)
    response = client.get(reverse("component_list"))
    assert response.status_code == 200
    object_list = response.context['object_list']
    assert object_list.count() == len(components)
    for item in components:
        assert item in object_list


@pytest.mark.django_db
def test_component_u_no_perm(user_perm_c_component, add_component):
    client = Client()
    client.force_login(user_perm_c_component)
    response = client.get(reverse('component_edit', kwargs={'pk': add_component.pk}))
    assert response.status_code == 403


@pytest.mark.django_db
def test_component_u_with_perm_get(user_perm_cru_component, add_component):
    client = Client()
    client.force_login(user_perm_cru_component)
    response = client.get(reverse('component_edit', kwargs={'pk': add_component.pk}))
    assert response.status_code == 200


@pytest.mark.django_db
def test_component_u_with_perm_post(user_perm_cru_component, add_component):
    client = Client()
    client.force_login(user_perm_cru_component)
    x = 'test 700 line'
    a = {
        'name': x, 'producer': x, 'catalogue_number': x
    }
    response = client.post(reverse('component_edit', kwargs={'pk': add_component.pk}), data=a)
    assert response.status_code == 302
    Component.objects.get(**a)


@pytest.mark.django_db
def test_component_d_no_perm(user_perm_c_component, add_component):
    client = Client()
    client.force_login(user_perm_c_component)
    response = client.get(reverse('component_delete', kwargs={'pk': add_component.pk}))
    assert response.status_code == 403


@pytest.mark.django_db
def test_component_u_with_perm_get(user_perm_crud_component, add_component):
    client = Client()
    client.force_login(user_perm_crud_component)
    response = client.get(reverse('component_delete', kwargs={'pk': add_component.pk}))
    assert response.status_code == 200


@pytest.mark.django_db
def test_component_u_with_perm_post(user_perm_crud_component, add_component):
    client = Client()
    client.force_login(user_perm_crud_component)
    response = client.post(reverse('component_delete', kwargs={'pk': add_component.pk}))
    assert response.status_code == 302
    with pytest.raises(ObjectDoesNotExist):
        Switchgear.objects.get(pk=add_component.pk)


# SwitchgearComponents VIEWS TESTS

@pytest.mark.django_db
def test_switchgearcomponents_no_login(add_switchgear):
    client = Client()
    response = client.get(reverse('switchgear_components_add', kwargs={'switchgear_id': add_switchgear.pk}))
    assert response.status_code == 302


@pytest.mark.django_db
def test_switchgearcomponents_no_perm(user, add_switchgear):
    client = Client()
    client.force_login(user)
    response = client.get(reverse('switchgear_components_add', kwargs={'switchgear_id': add_switchgear.pk}))
    assert response.status_code == 403


@pytest.mark.django_db
def test_switchgearcomponents_c_with_perm_get(user_perm_c_switchgearcomponents, add_switchgear):
    client = Client()
    client.force_login(user_perm_c_switchgearcomponents)
    response = client.get(reverse('switchgear_components_add', kwargs={'switchgear_id': add_switchgear.pk}))
    assert response.status_code == 200


@pytest.mark.django_db
def test_switchgearcomponents_c_with_perm_post(user_perm_c_switchgearcomponents, add_component, add_switchgear):
    client = Client()
    client.force_login(user_perm_c_switchgearcomponents)
    x = '1'
    a = {
        'component': add_component.pk, 'switchgear': add_switchgear.pk, 'amount_needed': x,
        'amount_missing': x
    }
    response = client.post(reverse('switchgear_components_add', kwargs={'switchgear_id': add_switchgear.pk}), data=a)
    assert response.status_code == 302
    SwitchgearComponents.objects.get(**a)


@pytest.mark.django_db
def test_switchgearcomponents_r_no_perm(user, add_switchgearcomponents, add_switchgear):
    client = Client()
    client.force_login(user)
    response = client.get(reverse('switchgear_components_detail', kwargs={'switchgear_id': add_switchgear.pk}))
    assert response.status_code == 403


@pytest.mark.django_db
def test_switchgearcomponents_r_no_perm(user_perm_cr_switchgearcomponents, add_switchgearcomponents, add_switchgear):
    client = Client()
    client.force_login(user_perm_cr_switchgearcomponents)
    response = client.get(reverse('switchgear_components_detail', kwargs={'switchgear_id': add_switchgear.pk}))
    assert response.status_code == 200


@pytest.mark.django_db
def test_switchgearcomponents_list_get_not_empty(user_perm_cr_switchgearcomponents,
                                                 switchgearcomponents, add_switchgear):
    client = Client()
    client.force_login(user_perm_cr_switchgearcomponents)
    response = client.get(reverse("switchgear_components_detail", kwargs={'switchgear_id': add_switchgear.pk}))
    assert response.status_code == 200
    object_list = response.context['object_list']
    assert object_list.count() == len(switchgearcomponents)
    for item in switchgearcomponents:
        assert item in object_list


@pytest.mark.django_db
def test_switchgearcomponents_u_no_perm(user, add_switchgearcomponents):
    client = Client()
    client.force_login(user)
    response = client.get(reverse('switchgear_components_edit', kwargs={'pk': add_switchgearcomponents.pk}))
    assert response.status_code == 403


@pytest.mark.django_db
def test_switchgearcomponents_u_with_perm_get(user_perm_cru_switchgearcomponents, add_switchgearcomponents):
    client = Client()
    client.force_login(user_perm_cru_switchgearcomponents)
    response = client.get(reverse('switchgear_components_edit', kwargs={'pk': add_switchgearcomponents.pk}))
    assert response.status_code == 200


@pytest.mark.django_db
def test_switchgearcomponents_u_with_perm_post(user_perm_cru_switchgearcomponents, add_switchgearcomponents,
                                               add_component, add_switchgear):
    client = Client()
    client.force_login(user_perm_cru_switchgearcomponents)
    x = '800'
    a = {
        'component': add_component.pk, 'switchgear': add_switchgear.pk, 'amount_needed': x,
        'amount_missing': x
    }
    response = client.post(reverse('switchgear_components_edit', kwargs={'pk': add_switchgearcomponents.pk}), data=a)
    assert response.status_code == 302
    SwitchgearComponents.objects.get(**a)


@pytest.mark.django_db
def test_switchgearcomponents_d_no_perm(user, add_switchgearcomponents):
    client = Client()
    client.force_login(user)
    response = client.get(reverse('switchgear_components_delete', kwargs={'pk': add_switchgearcomponents.pk}))
    assert response.status_code == 403


@pytest.mark.django_db
def test_switchgearcomponents_d_with_perm_get(user_perm_crud_switchgearcomponents, add_switchgearcomponents):
    client = Client()
    client.force_login(user_perm_crud_switchgearcomponents)
    response = client.get(reverse('switchgear_components_delete', kwargs={'pk': add_switchgearcomponents.pk}))
    assert response.status_code == 200


@pytest.mark.django_db
def test_switchgearcomponents_d_with_perm_post(user_perm_crud_switchgearcomponents, add_switchgearcomponents):
    client = Client()
    client.force_login(user_perm_crud_switchgearcomponents)
    response = client.post(reverse('switchgear_components_delete', kwargs={'pk': add_switchgearcomponents.pk}))
    assert response.status_code == 302
    with pytest.raises(ObjectDoesNotExist):
        SwitchgearComponents.objects.get(pk=add_switchgearcomponents.pk)
