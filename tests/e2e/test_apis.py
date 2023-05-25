from unicodedata import category
import pytest
from django.contrib.auth.hashers import make_password
from django.urls import reverse

from accounts.models import Member
from api.models import Product


@pytest.fixture
def get_user_plus_pass():
    password = "Wick"
    user = Member.objects.create(
        username = "john",
        password=make_password(password),
        email="test@test.test",
        is_superuser = True,
    )
    return user, password

@pytest.fixture
def get_user_plus_token(get_user_plus_pass, client):
    user, password = get_user_plus_pass
    url = reverse('token_obtain_pair')
    data = {
        "username": user,
        "password": password
    }
    response = client.post(url, data, secure=True)
    response_data = response.json()
    return user, response_data["access"]

@pytest.fixture(autouse=True)
def create_ten_products(get_user_plus_pass):
    """
    create 10 products for each test
    """
    user, password = get_user_plus_pass
    for x in range(10):
        Product.objects.create(
            name = f"product{x}",
            owner = user,
            category = f"type{x%2}",        # will be [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
            brand = f"brand{x%3}",          # will be [0, 1, 2, 0, 1, 2, 0, 1, 2, 0]
            price = x*1000,
            rating = round((10 - x) / 2)    # will be [5, 4, 4, 4, 3, 2, 2, 2, 1, 0]
        )
    return

@pytest.mark.django_db
def test_user_creation(get_user_plus_token):
    """
    please remember that each fixture will be run seprately for each test
    """
    assert Member.objects.count() == 2  # we created an admin user with migration files

@pytest.mark.django_db
def test_product_creation():
    assert Product.objects.count() == 10
    
@pytest.mark.django_db
def test_requests_without_token():
    assert 1 == 1
    assert 1 == 1
    assert 1 != 1
    assert 1 == 1
    
@pytest.mark.django_db
def test_filter_products_results():
    assert 1 == 1
