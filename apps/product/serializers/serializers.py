from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from apps.product.models.products import *


class CategorySerializer(serializers.ModelSerializer):
    products = SerializerMethodField('get_query', read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'products']

    def get_query(self, id):
        items = Product.objects.filter(category_id=id)
        serializer = ProductSerializer(instance=items, many=True)
        return serializer.data


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'
