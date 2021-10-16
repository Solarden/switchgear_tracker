import pytest
from django.contrib.auth.models import Permission

from tracker_app.models import Worker, Client, Company, Order, SwitchgearParameters, Switchgear, Component, \
    SwitchgearComponents


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
    u.user_permissions.add(p, p1)
    return u


@pytest.fixture
def user_perm_view_add_delete_client():
    p = Permission.objects.get(codename='view_client')
    p1 = Permission.objects.get(codename='add_client')
    p2 = Permission.objects.get(codename='delete_client')
    u = Worker.objects.create(username='testowy')
    u.user_permissions.add(p, p1, p2)
    return u


@pytest.fixture
def user_perm_view_add_delete_change_client():
    p = Permission.objects.get(codename='view_client')
    p1 = Permission.objects.get(codename='add_client')
    p2 = Permission.objects.get(codename='delete_client')
    p3 = Permission.objects.get(codename='change_client')
    u = Worker.objects.create(username='testowy')
    u.user_permissions.add(p, p1, p2, p3)
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


# USER PERMS COMPANY

@pytest.fixture
def user_perm_c_company():
    p = Permission.objects.get(codename='add_company')
    u = Worker.objects.create(username='test_user')
    u.user_permissions.add(p)
    return u


@pytest.fixture
def user_perm_cr_company():
    p = Permission.objects.get(codename='add_company')
    p1 = Permission.objects.get(codename='view_company')
    u = Worker.objects.create(username='test_user')
    u.user_permissions.add(p, p1)
    return u


@pytest.fixture
def user_perm_cru_company():
    p = Permission.objects.get(codename='add_company')
    p1 = Permission.objects.get(codename='view_company')
    p2 = Permission.objects.get(codename='change_company')
    u = Worker.objects.create(username='test_user')
    u.user_permissions.add(p, p1, p2)
    return u


@pytest.fixture
def user_perm_crud_company():
    p = Permission.objects.get(codename='add_company')
    p1 = Permission.objects.get(codename='view_company')
    p2 = Permission.objects.get(codename='change_company')
    p3 = Permission.objects.get(codename='delete_company')
    u = Worker.objects.create(username='test_user')
    u.user_permissions.add(p, p1, p2, p3)
    return u


@pytest.fixture
def add_company():
    return Company.objects.create(name='x', owner='x', nip='x', hq='x', prod='x', logo='x')


# USER PERMS Order

@pytest.fixture
def user_perm_c_order():
    p = Permission.objects.get(codename='add_order')
    u = Worker.objects.create(username='test_user')
    u.user_permissions.add(p)
    return u


@pytest.fixture
def user_perm_cr_order():
    p = Permission.objects.get(codename='add_order')
    p1 = Permission.objects.get(codename='view_order')
    u = Worker.objects.create(username='test_user')
    u.user_permissions.add(p, p1)
    return u


@pytest.fixture
def user_perm_cru_order():
    p = Permission.objects.get(codename='add_order')
    p1 = Permission.objects.get(codename='view_order')
    p2 = Permission.objects.get(codename='change_order')
    u = Worker.objects.create(username='test_user')
    u.user_permissions.add(p, p1, p2)
    return u


@pytest.fixture
def user_perm_crud_order():
    p = Permission.objects.get(codename='add_order')
    p1 = Permission.objects.get(codename='view_order')
    p2 = Permission.objects.get(codename='change_order')
    p3 = Permission.objects.get(codename='delete_order')
    u = Worker.objects.create(username='test_user')
    u.user_permissions.add(p, p1, p2, p3)
    return u


@pytest.fixture
def add_order(user, add_client):
    return Order.objects.create(order_name='x', ordered_by=add_client, added_by=user)


@pytest.fixture
def orders(user, add_client):
    lst = []
    for x in range(10):
        lst.append(Order.objects.create(order_name=x, ordered_by=add_client, added_by=user))
    return lst


# USER PERMS SwitchgearParameters

@pytest.fixture
def user_perm_c_switchgearparameters():
    p = Permission.objects.get(codename='add_switchgearparameters')
    u = Worker.objects.create(username='test_user')
    u.user_permissions.add(p)
    return u


@pytest.fixture
def user_perm_cr_switchgearparameters():
    p = Permission.objects.get(codename='add_switchgearparameters')
    p1 = Permission.objects.get(codename='view_switchgearparameters')
    u = Worker.objects.create(username='test_user')
    u.user_permissions.add(p, p1)
    return u


@pytest.fixture
def user_perm_cru_switchgearparameters():
    p = Permission.objects.get(codename='add_switchgearparameters')
    p1 = Permission.objects.get(codename='view_switchgearparameters')
    p2 = Permission.objects.get(codename='change_switchgearparameters')
    u = Worker.objects.create(username='test_user')
    u.user_permissions.add(p, p1, p2)
    return u


@pytest.fixture
def user_perm_crud_switchgearparameters():
    p = Permission.objects.get(codename='add_switchgearparameters')
    p1 = Permission.objects.get(codename='view_switchgearparameters')
    p2 = Permission.objects.get(codename='change_switchgearparameters')
    p3 = Permission.objects.get(codename='delete_switchgearparameters')
    u = Worker.objects.create(username='test_user')
    u.user_permissions.add(p, p1, p2, p3)
    return u


@pytest.fixture
def add_switchgearparameters():
    x = '12'
    return SwitchgearParameters.objects.create(name=x, par_a=x, par_ka=x, par_v=x, par_ui=x, par_hz=x, par_grid=x,
                                               par_protection=x, par_ip=x, par_ik=x)


@pytest.fixture
def switchgearparameters():
    lst = []
    for x in range(10):
        lst.append(
            SwitchgearParameters.objects.create(name=x, par_a=x, par_ka=x, par_v=x, par_ui=x, par_hz=x, par_grid=x,
                                                par_protection=x, par_ip=x, par_ik=x))
    return lst


# USER PERMS Switchgear

@pytest.fixture
def user_perm_c_switchgear():
    p = Permission.objects.get(codename='add_switchgear')
    u = Worker.objects.create(username='test_user')
    u.user_permissions.add(p)
    return u


@pytest.fixture
def user_perm_cr_switchgear():
    p = Permission.objects.get(codename='add_switchgear')
    p1 = Permission.objects.get(codename='view_switchgear')
    u = Worker.objects.create(username='test_user')
    u.user_permissions.add(p, p1)
    return u


@pytest.fixture
def user_perm_cru_switchgear():
    p = Permission.objects.get(codename='add_switchgear')
    p1 = Permission.objects.get(codename='view_switchgear')
    p2 = Permission.objects.get(codename='change_switchgear')
    u = Worker.objects.create(username='test_user')
    u.user_permissions.add(p, p1, p2)
    return u


@pytest.fixture
def user_perm_crud_switchgear():
    p = Permission.objects.get(codename='add_switchgear')
    p1 = Permission.objects.get(codename='view_switchgear')
    p2 = Permission.objects.get(codename='change_switchgear')
    p3 = Permission.objects.get(codename='delete_switchgear')
    u = Worker.objects.create(username='test_user')
    u.user_permissions.add(p, p1, p2, p3)
    return u


@pytest.fixture
def add_switchgear(add_order, add_switchgearparameters, user):
    x = 'x'
    return Switchgear.objects.create(order_ref=add_order, name=x, serial_no=x,
                                     switchgear_parameters=add_switchgearparameters, made_by=user)


@pytest.fixture
def switchgears(add_order, add_switchgearparameters, user):
    lst = []
    for x in range(10):
        lst.append(
            Switchgear.objects.create(order_ref=add_order, name=x, serial_no=x,
                                      switchgear_parameters=add_switchgearparameters, made_by=user))
    return lst


# USER PERMS Component

@pytest.fixture
def user_perm_c_component():
    p = Permission.objects.get(codename='add_component')
    u = Worker.objects.create(username='test_user')
    u.user_permissions.add(p)
    return u


@pytest.fixture
def user_perm_cr_component():
    p = Permission.objects.get(codename='add_component')
    p1 = Permission.objects.get(codename='view_component')
    u = Worker.objects.create(username='test_user')
    u.user_permissions.add(p, p1)
    return u


@pytest.fixture
def user_perm_cru_component():
    p = Permission.objects.get(codename='add_component')
    p1 = Permission.objects.get(codename='view_component')
    p2 = Permission.objects.get(codename='change_component')
    u = Worker.objects.create(username='test_user')
    u.user_permissions.add(p, p1, p2)
    return u


@pytest.fixture
def user_perm_crud_component():
    p = Permission.objects.get(codename='add_component')
    p1 = Permission.objects.get(codename='view_component')
    p2 = Permission.objects.get(codename='change_component')
    p3 = Permission.objects.get(codename='delete_component')
    u = Worker.objects.create(username='test_user')
    u.user_permissions.add(p, p1, p2, p3)
    return u


@pytest.fixture
def add_component():
    x = 'x'
    return Component.objects.create(name=x, producer=x, catalogue_number=x)


@pytest.fixture
def components():
    lst = []
    for x in range(10):
        lst.append(
            Component.objects.create(name=x, producer=x, catalogue_number=x))
    return lst


# USER PERMS SwitchgearComponents

@pytest.fixture
def user_perm_c_switchgearcomponents():
    p = Permission.objects.get(codename='add_switchgearcomponents')
    u = Worker.objects.create(username='test_user')
    u.user_permissions.add(p)
    return u


@pytest.fixture
def user_perm_cr_switchgearcomponents():
    p = Permission.objects.get(codename='add_switchgearcomponents')
    p1 = Permission.objects.get(codename='view_switchgearcomponents')
    u = Worker.objects.create(username='test_user')
    u.user_permissions.add(p, p1)
    return u


@pytest.fixture
def user_perm_cru_switchgearcomponents():
    p = Permission.objects.get(codename='add_switchgearcomponents')
    p1 = Permission.objects.get(codename='view_switchgearcomponents')
    p2 = Permission.objects.get(codename='change_switchgearcomponents')
    u = Worker.objects.create(username='test_user')
    u.user_permissions.add(p, p1, p2)
    return u


@pytest.fixture
def user_perm_crud_switchgearcomponents():
    p = Permission.objects.get(codename='add_switchgearcomponents')
    p1 = Permission.objects.get(codename='view_switchgearcomponents')
    p2 = Permission.objects.get(codename='change_switchgearcomponents')
    p3 = Permission.objects.get(codename='delete_switchgearcomponents')
    u = Worker.objects.create(username='test_user')
    u.user_permissions.add(p, p1, p2, p3)
    return u


@pytest.fixture
def add_switchgearcomponents(add_component, add_switchgear):
    x = '1'
    return SwitchgearComponents.objects.create(component=add_component, switchgear=add_switchgear, amount_needed=x,
                                               amount_missing=x)


@pytest.fixture
def switchgearcomponents():
    lst = []
    for x in range(10):
        lst.append(
            SwitchgearComponents.objects.create(component=add_component, switchgear=add_switchgear, amount_needed=x,
                                                amount_missing=x))
    return lst
