from django.db import models

# Create your models he

class Product(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=50, default=(""))
    category=models.CharField(max_length=50, default="")
    subcategory=models.CharField(max_length=50, default="")
    price=models.IntegerField(default=0)
    desc=models.CharField(max_length=300, default="")
    pub_date=models.DateField()
    image=models.ImageField(upload_to="shop/images", default="")
    
    def __str__(self):
        return self.product_name