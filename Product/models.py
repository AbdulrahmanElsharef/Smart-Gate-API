from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save,pre_save
from django.dispatch import receiver
from django.utils.text import slugify
import uuid
from django.contrib.auth.hashers import make_password


def CustomUser_directory(instance, filename):
    return f"Product/{instance.user.username}--{filename}"
class CustomUser(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(("Name"),max_length=100)
    phone=models.IntegerField(("Phone_Number"),unique=True)
    email=models.EmailField(("Email"),null=True,blank=True)
    password = models.CharField(("PassWord"),max_length=12)
    image = models.FileField(upload_to='CustomUser/image',null=True,blank=True,default='default.png')
    # slug = models.SlugField(null=True,blank=True)


    def __str__(self):
        return f" {self.username}"

    def save(self, *args, **kwargs):
        if self.password:
            self.password = make_password(self.password)
        self.slug = slugify(self.id)
        super(CustomUser, self).save(*args, **kwargs)



# @receiver(post_save,sender=User)
# def create_profile(sender,instance,created,**kwargs):
#     if created:
#         CustomUser.objects.create(
#             user=instance
#         )

class Room(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100,default="Room")
    image_url = models.URLField(null=True, blank=True)
    # slug = models.SlugField(null=True,blank=True)

    def __str__(self):
        return f" {self.title}"

    # def save(self, *args, **kwargs):
    #   self.slug = slugify(self.id)
    #   super(Room, self).save(*args, **kwargs)




def product_directory(instance, filename):
    return f"Product/{instance.name}--{filename}"

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    electricity_consumption = models.FloatField(default=0)
    image_url = models.FileField(upload_to=product_directory,max_length=200,null=True,blank=True)
    # Store actions as
    last_version_number = models.IntegerField(default=1)
    last_version_url = models.FileField(upload_to=f"Product/version_url/{product_directory}",max_length=200,null=True,blank=True)
    # slug = models.SlugField(null=True,blank=True)

    def __str__(self):
        return f" {self.name}"

    # def save(self, *args, **kwargs):
    #   self.slug = slugify(self.id)
    #   super(Product, self).save(*args, **kwargs)



class Product_Action(models.Model):
    product=models.ForeignKey(Product,verbose_name="Product", on_delete=models.PROTECT,related_name="Product_Action")
    # item=models.ForeignKey('Item',verbose_name="Item", on_delete=models.PROTECT,related_name="Product_Action")
    state = models.CharField(max_length=50,default="State")
    value = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.state}_{self.value}"

class Item_Action(Product_Action):
    item=models.ForeignKey('Item',verbose_name="Item", on_delete=models.PROTECT,related_name="Product_Action")


    def __str__(self):
        return f"{self.state}_{self.value}"

# @receiver(post_save, sender=Action)
# def set_switch_state_and_value(sender, instance, created, **kwargs):
#     if created:
#         # Here, you'll need to implement the logic to determine the switch_state based on the ID
#         # You can use a lookup table, a calculation, or any other method to set the appropriate state.
#         instance.state = f"switch_state-{instance.id}"
#         instance.save()

def update_directory(instance, filename):
    return f"Product/{instance.product.name}--{filename}"

class Update(models.Model):
    product=models.ForeignKey(Product,verbose_name="Product", on_delete=models.PROTECT,related_name="Product_Update")
    last_version_number = models.IntegerField(default=1)
    last_version_url = models.FileField(upload_to=f"Update/version_url/{update_directory}",max_length=200,null=True,blank=True)

    def __str__(self):
        return f"{self.id}_{self.product.name}"


class Item(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product = models.ForeignKey(Product,verbose_name="Product", related_name='Product_Items',on_delete=models.PROTECT)
    name = models.CharField(max_length=100,null=True, blank=True)
    mac_ip=models.CharField(max_length=100,null=True,blank=True,unique=True)
    is_assigned = models.BooleanField(default=False)
    last_version_number = models.IntegerField(default=1)
    do_update_now = models.BooleanField(default=False)
    users_list = models.ForeignKey(CustomUser,verbose_name="User", related_name='User_Item',on_delete=models.PROTECT)
    room=models.ForeignKey(Room,verbose_name="Room", on_delete=models.PROTECT,related_name="Room_Item")
    # slug = models.SlugField(null=True,blank=True)


    def __str__(self):
        return f"Item {self.id}:{self.name}"

    # def save(self, *args, **kwargs):
    #   self.slug = slugify(self.id)
    #   super(Item, self).save(*args, **kwargs)


class Voice_Command(models.Model):
    item=models.ForeignKey(Item,verbose_name="Item", on_delete=models.PROTECT,related_name="Item_Voice_Command")
    action_name = models.CharField(max_length=100,unique=True)
    action_state = models.IntegerField(default=0)
    command = models.CharField(max_length=250)

    def __str__(self):
        return f"{self.id}_{self.item.name}"


def AD_directory(instance, filename):
    return f"Product/{instance.title}--{filename}"

class AD(models.Model):
    title = models.CharField(max_length=50)
    message = models.TextField(max_length=255)
    ad_url = models.FileField(upload_to=f"AD/ad_url/{AD_directory}",null=True, blank=True)
    image = models.FileField(upload_to=f"AD/image/{AD_directory}",null=True, blank=True)
    video = models.FileField(upload_to=f'AD/ad_videos/{AD_directory}', null=True, blank=True)  # Optional video field

    def __str__(self):
        return self.title


class Complaint(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=250)
    status = models.CharField(max_length=50, default='Pending')
    customer=models.ForeignKey(CustomUser,verbose_name="Customer", on_delete=models.PROTECT,related_name="Customer_Complaint")  # Can be 'Pending', 'In Progress', 'Resolved'
    item=models.ForeignKey(Item,verbose_name="Item", on_delete=models.PROTECT,related_name="Item_Complaint",null=True,blank=True)  # Can be 'Pending', 'In Progress', 'Resolved'

    def __str__(self):
        return self.title