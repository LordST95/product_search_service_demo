from rest_framework import serializers

from api.models import Product, Cart, CartItem


class ProductSerializer(serializers.ModelSerializer):
    
    image_thumbnail = serializers.ImageField(read_only=True)

    class Meta:
        model = Product
        fields = "__all__"
        read_only_fields = ["rating", "owner"]
    
    def create(self, validated_data):
        user = self.context['request'].user
        product = Product.objects.create(owner = user, **validated_data)
        return product


class CartItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = CartItem
        fields = "__all__"


class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(source='cart_item_list_RM', many=True)

    class Meta:
        model = Cart
        exclude = ["buyer"]
