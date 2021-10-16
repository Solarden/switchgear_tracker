import pytest
from django.core.exceptions import ObjectDoesNotExist
from django.test import TestCase, Client
from django.urls import reverse
from .models import Client as ModelClient, Company

from tracker_app.models import Worker


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
        'username': 'zajaczek',
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
def test_client_list_with_login_no_perm(user):
    client = Client()
    client.force_login(user)
    response = client.get(reverse('client_list'))
    assert response.status_code == 403


@pytest.mark.django_db
def test_client_list_with_login_and_perm(user_perm_view_client):
    client = Client()
    client.force_login(user_perm_view_client)
    response = client.get(reverse('client_list'))
    assert response.status_code == 200


@pytest.mark.django_db
def test_client_list_get_not_empty(clients, user_perm_view_client):
    client = Client()
    client.force_login(user_perm_view_client)
    response = client.get(reverse("client_list"))
    assert response.status_code == 200
    client_list = response.context['object_list']
    assert client_list.count() == len(clients)
    for client in clients:
        assert client in client_list


@pytest.mark.django_db
def test_add_client_post_with_perm(user_perm_view_add_client):
    client = Client()
    client.force_login(user_perm_view_add_client)
    a = {
        'name': 'pawel',
    }
    response = client.post(reverse('client_add'), data=a)
    assert response.status_code == 302
    ModelClient.objects.get(**a)


@pytest.mark.django_db
def test_remove_client_no_perm(user_perm_view_add_client, add_client):
    client = Client()
    client.force_login(user_perm_view_add_client)
    response = client.get(reverse("client_delete", kwargs={'pk': add_client.pk}))
    assert response.status_code == 403


@pytest.mark.django_db
def test_delete_client_with_perm(user_perm_view_add_delete_client, add_client):
    client = Client()
    client.force_login(user_perm_view_add_delete_client)
    response = client.post(reverse("client_delete", kwargs={'pk': add_client.pk}))
    assert response.status_code == 302
    with pytest.raises(ObjectDoesNotExist):
        ModelClient.objects.get(pk=add_client.pk)


@pytest.mark.django_db
def test_change_client_with_no_perm(user_perm_view_add_delete_client, add_client):
    client = Client()
    client.force_login(user_perm_view_add_delete_client)
    response = client.get(reverse('client_edit', kwargs={'pk': add_client.pk}))
    assert response.status_code == 403


@pytest.mark.django_db
def test_change_client_with_perm(user_perm_view_add_delete_change_client, add_client):
    client = Client()
    client.force_login(user_perm_view_add_delete_change_client)
    a = {
        'name': 'test_change'
    }
    response = client.post(reverse('client_edit', kwargs={'pk': add_client.pk}), data=a)
    assert response.status_code == 302
    ModelClient.objects.get(**a)


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

# SwitchgearParameters VIEWS TESTS

# Switchgear VIEWS TESTS

# Component VIEWS TESTS

# SwitchgearComponents VIEWS TESTS
