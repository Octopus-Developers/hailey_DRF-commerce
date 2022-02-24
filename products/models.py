from django.db import models


class Tag(models.Model):
    tag_name = models.CharField(max_length=15, unique=True)
    
    def __str__(self):
        return f'{self.tag_name}'
        
    class Meta:
        db_table = "tags"
    

class Product(models.Model):
    product_name        = models.CharField(max_length=30, unique=True)
    thumbnail_image_url = models.URLField(max_length=3000, null=True)
    price               = models.PositiveIntegerField()
    net_price           = models.PositiveIntegerField()
    is_sold_out         = models.BooleanField(null=True, default=False)
    created_at          = models.DateTimeField(auto_now_add=True)
    updated_at          = models.DateTimeField(auto_now=True, null=True)
    tags                = models.ManyToManyField(Tag, through='TagList')
        
    def __str__(self):
        return f'{self.tags}'
    
    class Meta:
        db_table = "products"
    
class TagList(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)