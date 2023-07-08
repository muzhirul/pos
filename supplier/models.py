from django.db import models
from django_userforeignkey.models.fields import UserForeignKey

# Create your models here.
class Supplier(models.Model):
    name = models.CharField(max_length=255,verbose_name='Supplier Name')
    slug = models.SlugField(max_length=255,verbose_name="Supplier Slug")
    c_person = models.CharField(max_length=255,verbose_name='Contact Person')
    address = models.TextField(null=True,blank=True,verbose_name='Supplier Address')
    mobile = models.CharField(max_length=20,verbose_name='Supplier Mobile')
    status = models.BooleanField(default=True)
    created_by = UserForeignKey(auto_user_add=True, on_delete=models.SET_NULL,related_name='supplier_creator', editable=False, blank=True, null=True)
    last_modified_by = UserForeignKey(auto_user=True, on_delete=models.SET_NULL, related_name='supplier_updated_by', editable=False, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'supplier'
        verbose_name = 'Supplier'

    def __str__(self):
        return self.name