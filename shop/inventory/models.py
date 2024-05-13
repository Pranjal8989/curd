from django.db import models

# Create your models here.
class category(models.Model):
    name=models.CharField(max_length=45,null=False)
    def __str__(self):
        return self.name

class size(models.Model):
    name=models.CharField(max_length=45,null=False)
    def __str__(self):
        return self.name

class Color(models.Model):
    color_name=models.CharField(max_length=45,null=False)
    def __str__(self):
        return self.color_name

class Product(models.Model):
    product_name= models.CharField(max_length=45,null=False)
    category = models.IntegerField(null=False)
    size =  models.IntegerField(null=False)
    color= models.IntegerField(null=False)
    material=  models.CharField(max_length=45,null=False)
    price =  models.IntegerField(null=False)
    quantity= models.IntegerField(null=False)
    image= models.FileField( upload_to="product", max_length=250 , null=True, default=None)
    description=models.CharField(max_length=45)

    def __str__(self):
        return self.product_name