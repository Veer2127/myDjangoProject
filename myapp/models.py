from django.db import models
from datetime import datetime

# Create your models here.

class Contact(models.Model):
    fname=models.CharField(max_length=50)
    lname=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    phone=models.CharField(max_length=10)
    message=models.TextField()

    def __str__(self):
        return self.fname
    
class User(models.Model):
    fname=models.CharField(max_length=50)
    lname=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    phone=models.CharField(max_length=10)
    address=models.TextField()
    password=models.CharField(max_length=10)
    cpassword=models.CharField(max_length=10)
    usertype=models.CharField(max_length=40)
    profile_pic=models.ImageField('profile_pic/',default="")


    def __str__(self):
        return self.fname+ " " + self.lname

class Product(models.Model):
    seller=models.ForeignKey(User,on_delete=models.CASCADE)
    product_name=models.CharField(max_length=40)
    product_price=models.CharField(max_length=10)
    product_image=models.ImageField(upload_to="media/")
    product_description=models.TextField() 

    def __str__(self):
        return self.product_name  

class Wishlist(models.Model):
   user=models.ForeignKey(User,on_delete=models.CASCADE)
   product=models.ForeignKey(Product,on_delete=models.CASCADE)
   date=models.DateTimeField(default=datetime.now)

 

class Cart(models.Model):
   user=models.ForeignKey(User,on_delete=models.CASCADE)
   product=models.ForeignKey(Product,on_delete=models.CASCADE)
   date=models.DateTimeField(default=datetime.now)
   product_price=models.PositiveIntegerField()
   product_qty=models.PositiveIntegerField(default=1)
   total_price=models.PositiveIntegerField()
   shipping=models.PositiveIntegerField(default=10)

   
