from django.db import models
from django_userforeignkey.models.fields import UserForeignKey

# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=255, verbose_name="Brand Name")
    slug = models.SlugField(max_length=255,verbose_name="Brand Slug")
    description = models.TextField(null=True)
    created_by = UserForeignKey(auto_user_add=True, on_delete=models.SET_NULL,related_name='brand_creator', editable=False, blank=True, null=True)
    last_modified_by = UserForeignKey(auto_user=True, on_delete=models.SET_NULL, related_name='brand_updated_by', editable=False, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'brand'
        verbose_name = 'Brand'
    
    def __str__(self):
        return self.name
    
