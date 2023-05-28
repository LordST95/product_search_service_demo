from celery import shared_task
from celery.utils.log import get_logger
from celery.utils.log import get_task_logger

logger = get_logger(__name__)
logger2 = get_task_logger(__name__)

@shared_task
def send_welcome_email(user, **kwargs):
    logger.info(f"Task is running for user: {user}")
    
    # TODO
    print(user)
    logger.info(f'logger2   {user}')
        
    logger.info(f"Task is done for user: {user}")
