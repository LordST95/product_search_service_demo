from celery import shared_task
from celery.utils.log import get_logger


logger = get_logger(__name__)


@shared_task
def upload_image(user, image, **kwargs):
    logger.info(f"Task is running for user: {user}")
    # TODO
    logger.info(f"Task is done for user: {user}")
