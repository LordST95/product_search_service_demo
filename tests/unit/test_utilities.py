from io import BytesIO

import pytest
from django.core.files.uploadedfile import SimpleUploadedFile
from PIL import Image

from api.models import Product
from api.tasks import upload_image


@pytest.mark.django_db
def test_uploadImage(get_user_plus_token, get_image_for_upload):
    user, token = get_user_plus_token
    product = Product.objects.filter(owner=user)[0]
    image = get_image_for_upload
    product.another_image.save(image.name, image)
    
    upload_image(user.username, product.id)
    
    product.refresh_from_db()
    assert product.another_image.height == 200
    assert product.another_image.width == 200
    assert product.another_image_thumbnail.height == 60
    assert product.another_image_thumbnail.width == 60
