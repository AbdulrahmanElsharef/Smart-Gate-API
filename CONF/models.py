from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save,pre_save
from django.dispatch import receiver
from django.utils.text import slugify
import uuid
from django.contrib.auth.hashers import make_password


class UOM(models.Model):
    name = models.CharField("UOM",max_length=50, unique=True)
    created=models.DateTimeField(("Created"),auto_now=True)
    updated=models.DateTimeField(("Updated"),auto_now_add=True)
    note = models.CharField("Note",max_length=200, null=True,blank=True)    
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "UOM"




class WHSBranch(models.Model):
    name = models.CharField("Branch",max_length=50, unique=True)
    detail = models.CharField("Detail",max_length=200)
    created=models.DateTimeField(("Created"),auto_now=True)
    updated=models.DateTimeField(("Updated"),auto_now_add=True)
    note = models.CharField("Note",max_length=200, null=True,blank=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "WHS_Branch"

    
    

class Color(models.Model):
    name = models.CharField("Color",max_length=50, unique=True)
    created=models.DateTimeField(("Created"),auto_now=True)
    updated=models.DateTimeField(("Updated"),auto_now_add=True)
    note = models.CharField("Note",max_length=200, null=True,blank=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "COLOR"

class Brand(models.Model):
    name = models.CharField("Brand",max_length=50, unique=True)
    created=models.DateTimeField(("Created"),auto_now=True)
    updated=models.DateTimeField(("Updated"),auto_now_add=True)
    note = models.CharField("Note",max_length=200, null=True,blank=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "BRAND"
    
    
class MainCategory(models.Model):
    name = models.CharField("MainCategory",max_length=50, unique=True)
    created=models.DateTimeField(("Created"),auto_now=True)
    updated=models.DateTimeField(("Updated"),auto_now_add=True)
    note = models.CharField("Note",max_length=200, null=True,blank=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "MAIN_CAT"
    
    
class SubCategory(models.Model):
    main = models.ForeignKey(MainCategory,verbose_name="Main", related_name='MainCategory', on_delete=models.PROTECT,)
    name = models.CharField("SubCategory",max_length=50, unique=True)
    created=models.DateTimeField(("Created"),auto_now=True)
    updated=models.DateTimeField(("Updated"),auto_now_add=True)
    note = models.CharField("Note",max_length=200, null=True,blank=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "SUP_CAT"
    
    
class Category(models.Model):
    sub_category= models.ForeignKey(SubCategory,verbose_name="SubCategory", related_name='SubCategory', on_delete=models.PROTECT,)
    name = models.CharField("Category",max_length=50, unique=True)
    created=models.DateTimeField(("Created"),auto_now=True)
    updated=models.DateTimeField(("Updated"),auto_now_add=True)
    note = models.CharField("Note",max_length=200, null=True,blank=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "CATEGORY"

class Supplier(models.Model):
    name = models.CharField("Supplier",max_length=50, unique=True)
    phone = models.CharField("Phone",max_length=50, unique=True)
    created=models.DateTimeField(("Created"),auto_now=True)
    updated=models.DateTimeField(("Updated"),auto_now_add=True)
    note = models.CharField("Note",max_length=200, null=True,blank=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "SUPPLIER"
    
class Customer(models.Model):
    name = models.CharField("Customer",max_length=50, unique=True)
    phone = models.CharField("Phone",max_length=50, unique=True)
    created=models.DateTimeField(("Created"),auto_now=True)
    updated=models.DateTimeField(("Updated"),auto_now_add=True)
    note = models.CharField("Note",max_length=200, null=True,blank=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "CUSTOMER"


