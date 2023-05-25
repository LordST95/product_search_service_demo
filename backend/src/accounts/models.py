from django.contrib.auth.models import AbstractUser


class Member(AbstractUser):

    def __str__(self):
        return self.username
