from django.db import migrations
from django.contrib.auth.hashers import make_password
from django.conf import settings


def create_superuser(apps, schema_editor):
    User = apps.get_model('accounts', 'Member')
    User(
        first_name=settings.MAIN_ADMIN_F_NAME,
        last_name=settings.MAIN_ADMIN_L_NAME,
        username = settings.MAIN_ADMIN_USER,
        password=make_password(settings.MAIN_ADMIN_PASS),
        email=settings.MAIN_ADMIN_EMAIL,
        is_active = True,
        is_superuser = True,
        is_staff = True
        ).save()

class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_superuser),
    ]
