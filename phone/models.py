from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=225)
    
    class Meta:
        ordering=("name",)
        verbose_name_plural = "Categories"
    def __str__(self):
        return self.name

class Phone(models.Model):
    category=models.ForeignKey(Category,related_name='phone',on_delete=models.CASCADE)
    name = models.CharField(max_length=225)
    destription =models.TextField(blank=True,null=True)
    price = models.FloatField()
    image=models.ImageField(upload_to='phone_images',blank=True,null=True)
    is_sold=models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)
    Created_by=models.ForeignKey(User,related_name='phones',on_delete=models.CASCADE)
   
    class Meta:
        ordering=("name",)

    def __str__(self):
        return self.name
