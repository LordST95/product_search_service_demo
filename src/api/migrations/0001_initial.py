# Generated by Django 4.2.1 on 2023-05-25 19:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('category', models.CharField(blank=True, max_length=15, null=True)),
                ('brand', models.CharField(blank=True, max_length=15, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('rating', models.FloatField(blank=True, null=True)),
                ('image', models.ImageField(default='default_product.png', upload_to='product_images')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_list_RM', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
