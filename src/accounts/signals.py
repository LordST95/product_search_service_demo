from datetime import datetime, timedelta

from django.db.models.signals import post_save
from django.dispatch import receiver

from accounts.models import Member
from accounts.tasks import send_welcome_email


@receiver(post_save, sender=Member, dispatch_uid="send_email_for_new_users")
def send_email(sender, instance=None, created=False, **kwargs):
    if created:
        # sending_time = datetime.now() + timedelta(seconds=5, days=1)
        sending_time = datetime.now() + timedelta(seconds=10)
        if instance.email:
            send_welcome_email.apply_async(args=(instance.username, instance.email), eta=sending_time)
    return "sth"
