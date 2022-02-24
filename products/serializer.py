from rest_framework          import serializers
from .models                 import Product, Tag, TagList
from django.db               import transaction
from django.core.exceptions  import ObjectDoesNotExist

class CreatableSlugRelatedField(serializers.SlugRelatedField):
    
    def to_internal_value(self, data):
        try:
            return self.get_queryset().get(**{self.slug_field: data})
        except ObjectDoesNotExist:
            return self.get_queryset().create(**{self.slug_field: data})
        except (TypeError, ValueError):
            self.fail('invalid')

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model        = Tag
        fields       = ['tag_name']
        extra_kwargs = {
            'tag_name' : {
                'validators' : []
            }
        }

class TagListSerializer(serializers.ModelSerializer):
    class Meta:
        model  = TagList
        fields = ['tag']

class ProductSerializer(serializers.ModelSerializer):
    created_at    = serializers.DateTimeField(read_only=True)
    updated_at    = serializers.DateTimeField(read_only=True)
    discount_rate = serializers.SerializerMethodField(method_name='get_discount_rate')
    tags          = CreatableSlugRelatedField(many=True, queryset=Tag.objects.all(), slug_field='tag_name')

    class Meta:
        model  = Product
        fields = ['product_name','thumbnail_image_url', 'price', 
                  'net_price','is_sold_out', 'discount_rate', 'tags', 'created_at', 'updated_at']
    
    @transaction.atomic() 
    def create(self, validated_data):
        if validated_data['price'] > validated_data['net_price']:
            raise serializers.ValidationError("상품 가격과 정가를 재확인하십시오.")
        
        validated_tags = validated_data.pop('tags')
        product = self.Meta.model.objects.create(**validated_data)
        
        for tag in validated_tags:
            obj, created = Tag.objects.get_or_create(tag_name=tag, defaults={'tag_name':tag})
            product.tags.add(obj)

        product.save()
        return product

    def get_discount_rate(self, obj):
        discount_value = int((1 - obj.price / obj.net_price) * 100)
        return discount_value