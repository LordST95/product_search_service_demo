from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


class Product(models.Model):
    
    name = models.CharField(max_length=30)
    owner = models.ForeignKey(
        'accounts.Member', related_name='product_list_RM', on_delete=models.CASCADE
    )
    category = models.CharField(max_length=15, blank=True, null=True)
    brand = models.CharField(max_length=15, blank=True, null=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)         # Always use DecimalField for money; Even simple operations (addition, subtraction) are not immune to float rounding issues.
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    rating = models.FloatField(blank=True, null=True)
    image = models.ImageField(
        upload_to='product_images', default='default_product.png'
    )
    image_thumbnail = ImageSpecField(
        source='image',
        processors=[ResizeToFill(100, 100)],
        format='JPEG',
        options={'quality': 60}
    )
    
    def __str__(self):
        return self.name
