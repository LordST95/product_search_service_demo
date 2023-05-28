from celery import shared_task
from celery.utils.log import get_logger
from django.core.mail import send_mail
from django.conf import settings

logger = get_logger(__name__)

@shared_task
def send_welcome_email(username, email, **kwargs):
    logger.info(f"Task is running for sending email to: {username}")
    
    send_mail(
        "Welcome to our site",
        f"""
        Dear {username},
        Please consider our warm welcome. We are so glad for your joining.
        
        Best regards,
        Sina
        """,
        settings.EMAIL_HOST_USER,
        [email],
        fail_silently=False,
    )
        
    logger.info(f"Email was sent to: {username}")
