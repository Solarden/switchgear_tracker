import pytest
from django.test import TestCase, Client
from django.urls import reverse
from .models import Client as ModelClient

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


# @pytest.mark.django_db
# def test_signup_post_register():
#     client = Client()
#     a = {
#         'username': 'testowy',
#         'email': 'test@test.pl',
#         'first_name': 'pawel',
#         'last_name': 'testowy',
#         'password1': 'tymczasowe',
#         'password2': 'tymczasowe',
#     }
#     response = client.post(reverse("signup"), data=a)
#     assert response.status_code == 200
#     Worker.objects.get(**a)

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
def test_remove_client_no_perm(user_perm_view_add_client):
    client = Client()
    client.force_login(user_perm_view_add_client)
    a = {
        'name': 'pawel',
    }
    response = client.post(reverse('client_add'), data=a)
    assert response.status_code == 302
    response = client.get(reverse("client_delete", kwargs={'pk': 1}))
    assert response.status_code == 403


@pytest.mark.django_db
def test_delete_client_with_perm(user_perm_view_add_delete_client):
    client = Client()
    client.force_login(user_perm_view_add_delete_client)
    ModelClient.objects.create(name='pawel')
    response = client.post(reverse("client_delete", kwargs={'pk': 1}))
    assert response.status_code == 302
