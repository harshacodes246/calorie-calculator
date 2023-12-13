from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name=models.CharField(max_length=200,null=True)
    email=models.CharField(max_length=200,null=True)
    date_created=models.DateTimeField(auto_now_add=True,null=True)
    
    def __str__(self):
        return str(self.name)
class Category(models.Model):
    options=(
        ('breakfast','breakfast'),
        ('lunch','lunch'),
        ('dinner','dinner'),
        ('snacks','snacks'),
    )
    name=models.CharField(max_length=50,choices=options)
    def __str__(self):
        return self.name
class Fooditem(models.Model):
    fitm = models.CharField(max_length=200)
    calo = models.DecimalField(max_digits=5,decimal_places=2,default=0)
    carbo = models.DecimalField(max_digits=5,decimal_places=2,default=0)
    fat = models.DecimalField(max_digits=5,decimal_places=2,default=0)
    prot = models.DecimalField(max_digits=5,decimal_places=2,default=0)
    
    
    def __str__(self):
        return str(self.fitm)
# for user page-------------------------------------------------------------
# class UserFooditem(models.Model):
#     customer = models.ManyToManyField(Customer ,blank=True)
#     fooditem=models.ManyToManyField(Fooditem)


class reg_tbl(models.Model):
    unm=models.CharField(max_length=50)
    em1=models.EmailField()
    psc1=models.CharField(max_length=16)
    def __str__(self):
        return self.unm