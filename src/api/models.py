from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

from accounts.models import Member


class Product(models.Model):
    
    name = models.CharField(max_length=30)
    owner = models.ForeignKey(
        Member, related_name='product_list_RM', on_delete=models.CASCADE
    )
    category = models.CharField(max_length=15, blank=True, null=True)
    brand = models.CharField(max_length=15, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)         # Always use DecimalField for money; Even simple operations (addition, subtraction) are not immune to float rounding issues.
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
    # below fields added just for parallel task (item #12 in project description)
    another_image = models.ImageField(
        upload_to='another_product_images', blank=True, null=True
    )
    another_image_thumbnail = models.CharField(max_length=150, blank=True, null=True)
    
    def __str__(self):
        return self.name


class Cart(models.Model):

    buyer = models.ForeignKey(Member, related_name='cart_list_RM', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    is_paid = models.BooleanField(default=False)
    # each cart, has some items which defined in the CartItem
    
    @property
    def itemsCount(self):
        return self.cart_item_list_RM.all().count()

    @property
    def productsList(self):
        return [x.name for x in self.cart_item_list_RM.all()]

    @property
    def totalPrice(self):
        price = 0
        for x in self.cart_item_list_RM.all():
            price += x.price
        return price

    def __str__(self):
        return f"{self.id} | {self.buyer} | {self.created_at}"


class CartItem(models.Model):
    
    cart = models.ForeignKey(Cart, related_name='cart_item_list_RM',on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='cart_item_list_RM', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    @property
    def price(self):
        return self.product.price

    def __str__(self):
        return f"{self.cart} | {self.product}"
