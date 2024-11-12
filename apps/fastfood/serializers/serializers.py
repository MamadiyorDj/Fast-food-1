from rest_framework.serializers import ModelSerializer
from apps.fastfood.models.fastfoods import *
from apps.fastfood.models.fastfood_product import *


class FastFoodSerializer(ModelSerializer):
    class Meta:
        model = Fastfood
        fields = '__all__'


class FastFoodParentSerializer(ModelSerializer):
    class Meta:
        model = FastFoodParent
        fields = '__all__'