import os
import pathlib
from io import BytesIO

from celery import shared_task
from celery.utils.log import get_logger
from django.conf import settings
from PIL import Image

from api.models import Product


logger = get_logger(__name__)


@shared_task
def upload_image(user, product_id, **kwargs):
    logger.info(f"Task is running for user: {user}")
    
    product = Product.objects.get(id=product_id)
    image = product.another_image
    file_name = str(image.name).split("/")[-1]   # value format ==> sth.jpeg
    with Image.open(image.file) as im:
        im.thumbnail((60, 60))
        thumb_io = BytesIO()  # create a BytesIO object
        im.save(thumb_io, "JPEG")
        product.another_image_thumbnail.save(f"thumb_{file_name}", thumb_io)
        
    logger.info(f"Task is done for user: {user}")
