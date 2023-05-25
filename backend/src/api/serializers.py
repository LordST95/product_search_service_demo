from rest_framework import serializers

from api.models import Product


class ProductListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = "__all__"


class ProductCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        exclude = ["rating"]
