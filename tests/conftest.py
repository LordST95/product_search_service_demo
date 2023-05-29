from io import BytesIO
import pathlib

import pytest
from django.contrib.auth.hashers import make_password
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from PIL import Image

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
            quantity = x,
            rating = (10 - x) / 2    # will be [5.0, 4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0.5]
        )
    return


@pytest.fixture
def get_image_for_upload():
    # covert png to jpeg
    current_dir = pathlib.Path().absolute()
    path = current_dir.parent.joinpath("src", "media_server_folder", "default_product.png")
    im = Image.open(path)
    rgb_im = im.convert('RGB')
    thumb_io = BytesIO()  # create a BytesIO object
    rgb_im.save(thumb_io, "JPEG")
    thumb_io.seek(0)
    image = SimpleUploadedFile(
        "default_product.jpg", thumb_io.read(),
        content_type="image/jpeg"
    )
    return image
