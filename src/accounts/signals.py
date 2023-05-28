from datetime import datetime, timedelta

from django.db.models.signals import post_save
from django.dispatch import receiver

from accounts.models import Member
from accounts.tasks import send_welcome_email


@receiver(post_save, sender=Member, dispatch_uid="send_email_for_new_users")
def send_email(sender, instance=None, created=False, **kwargs):
    if created:
        today = datetime.now()
        # sending_time = today + timedelta(seconds=5, days=1)
        sending_time = today + timedelta(seconds=10)
        print(f"{sending_time= }")
        # method1 ==> task does not start in the windows :|
        # result = send_welcome_email.apply_async(args=(instance.username,), eta=sending_time)
        # # .get() forced it to wait
        # result_output = result.get()
        # method2
        if instance.email:
            send_welcome_email.delay(instance.username, instance.email)
        
    return "sth"
