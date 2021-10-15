import pytest
from django.contrib.auth.models import User, Permission

from tracker_app.models import Worker, Client


@pytest.fixture
def user():
    return Worker.objects.create(username='testowy')


# USER PERMS CLIENT

@pytest.fixture
def user_perm_view_client():
    p = Permission.objects.get(codename='view_client')
    u = Worker.objects.create(username='testowy')
    u.user_permissions.add(p)
    return u


@pytest.fixture
def user_perm_view_add_client():
    p = Permission.objects.get(codename='view_client')
    p1 = Permission.objects.get(codename='add_client')
    u = Worker.objects.create(username='testowy')
    u.user_permissions.add(p)
    u.user_permissions.add(p1)
    return u


@pytest.fixture
def user_perm_view_add_delete_client():
    p = Permission.objects.get(codename='view_client')
    p1 = Permission.objects.get(codename='add_client')
    p2 = Permission.objects.get(codename='delete_client')
    u = Worker.objects.create(username='testowy')
    u.user_permissions.add(p)
    u.user_permissions.add(p1)
    u.user_permissions.add(p2)
    return u


@pytest.fixture
def user_perm_view_add_delete_change_client():
    p = Permission.objects.get(codename='view_client')
    p1 = Permission.objects.get(codename='add_client')
    p2 = Permission.objects.get(codename='delete_client')
    p3 = Permission.objects.get(codename='change_client')
    u = Worker.objects.create(username='testowy')
    u.user_permissions.add(p)
    u.user_permissions.add(p1)
    u.user_permissions.add(p2)
    u.user_permissions.add(p3)
    return u


@pytest.fixture
def clients():
    lst = []
    for x in range(10):
        lst.append(Client.objects.create(name=x))
    return lst


@pytest.fixture
def add_client():
    return Client.objects.create(name='x')
