from rest_framework import serializers

from api.models import Product, Cart, CartItem


class ProductListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = "__all__"


class ProductCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        exclude = ["rating"]


class CartItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = CartItem
        fields = "__all__"


class CartListSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(source='cart_item_list_RM', many=True)

    class Meta:
        model = Cart
        exclude = ["buyer"]
