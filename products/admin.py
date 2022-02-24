from django.contrib              import admin
from django.utils.safestring     import mark_safe
from .models                     import Product, Tag, TagList
from products                    import serializer
from .serializer                 import CreatableSlugRelatedField
from django_admin_relation_links import AdminChangeLinksMixin


class TagInLine(admin.StackedInline):
    model = TagList
    extra = 2


@admin.register(Product)
class ProductAdmin(AdminChangeLinksMixin, admin.ModelAdmin):
    serializer_class = serializer.ProductSerializer
    tags = CreatableSlugRelatedField(many=True, queryset=Tag.objects.all(), slug_field='tag_name')
    
    list_display    = ["product_name", "get_thumbnail_image_url","price", "is_sold_out", "created_at", "tags", "get_discount_rate"]
    readonly_fields = ["get_discount_rate"]
    search_fields   = ["product_name"]
    change_links    = ['tags']
    inlines         = [TagInLine]
    
    def get_thumbnail_image_url(self, obj):
        return mark_safe('<img src="{}" style="width:100px; height:auto;">'.format(obj.thumbnail_image_url))

    def get_discount_rate(self, obj):
        discount_value = int((1 - obj.price / obj.net_price) * 100)
        return discount_value
    
@admin.register(Tag)
class TagAdmin(AdminChangeLinksMixin, admin.ModelAdmin):
    list_display     = ["tag_name"]
    changelist_links = ['tags']
    
    def tag_name(self, obj):
        return obj.tag

admin.site.site_header = "Product Admin"
