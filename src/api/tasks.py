import os
import pathlib

from celery import shared_task
from celery.utils.log import get_logger
from django.conf import settings
from PIL import Image

from api.models import Product


logger = get_logger(__name__)


@shared_task
def upload_image(user, product_id, absolute_url, **kwargs):
    logger.info(f"Task is running for user: {user}")
    
    product = Product.objects.get(id=product_id)
    image = product.another_image
    file_name = str(image.name).split("/")[-1]   # value format ==> sth.jpeg
    with Image.open(image.file) as im:
        im.thumbnail((60, 60))
        saved_path = settings.MEDIA_ROOT.joinpath("another_image_thumbnail", file_name)
        im.save(saved_path, "JPEG")
    
    thumbnail_url = absolute_url+settings.MEDIA_URL+"another_image_thumbnail/"+file_name
    product.another_image_thumbnail = thumbnail_url
    product.save()
    
    logger.info(f"Task is done for user: {user}")
