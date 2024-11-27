from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import *
from django.dispatch import receiver
from django.utils.text import slugify
import uuid
from django.contrib.auth.hashers import make_password
from CONF.models import *
from django.utils import timezone
from django.db.models import Sum

    
class Item(models.Model):
    id = models.IntegerField("Barcode",primary_key=True,unique=True)
    sku = models.CharField('Sku',max_length=50, unique=True,null=True,blank=True)
    name = models.CharField('Name',max_length=50,default="Description")
    uom = models.ForeignKey(UOM,verbose_name="Uom", related_name='Item_uom', on_delete=models.PROTECT,)
    color = models.ForeignKey(Color,verbose_name="Color", related_name='Item_Color', on_delete=models.PROTECT,)
    brand = models.ForeignKey(Brand,verbose_name="Brand", related_name='Item_Brand', on_delete=models.PROTECT,)
    category = models.ForeignKey(Category,verbose_name="Category", related_name='Item_Category', on_delete=models.PROTECT,)
    safety=models.IntegerField(("Safety"),default=0)
    rdp=models.DecimalField(("RDP"), max_digits=8, decimal_places=2,default=0)
    rrp=models.DecimalField(("RRP"), max_digits=8, decimal_places=2,default=0)
    created=models.DateTimeField(("Created"),auto_now=True)
    updated=models.DateTimeField(("Updated"),auto_now_add=True)
    note = models.CharField("Note",max_length=50, null=True,blank=True)

    def __str__(self):
        return str(self.id)
    class Meta:
        verbose_name_plural = "ITEMS"
        
        
    def Stock(self):
        total_in = self.Stock_IN_Detail_item.aggregate(total_quantity=Sum('quantity'))['total_quantity'] or 0
        total_out = self.Stock_Out_Detail_item.aggregate(total_quantity=Sum('quantity'))['total_quantity'] or 0
        # total_sales = self.Sales_Order_item.aggregate(total_quantity=Sum('quantity'))['total_quantity'] or 0
        return total_in - total_out 

    def Total_In(self):
        total_in = self.Stock_IN_Detail_item.aggregate(total_quantity=Sum('quantity'))['total_quantity'] or 0
        # total_sales = self.Sales_Order_item.aggregate(total_quantity=Sum('quantity'))['total_quantity'] or 0
        return total_in
      
    def Total_out(self):
        total_out = self.Stock_Out_Detail_item.aggregate(total_quantity=Sum('quantity'))['total_quantity'] or 0
        # total_sales = self.Sales_Order_item.aggregate(total_quantity=Sum('quantity'))['total_quantity'] or 0
        return total_out   
    
    def Status(self):
        stock=self.Stock()
        if stock == self.safety:
            return "Stable"
        elif stock > self.safety:
            return f"Over-{stock-self.safety}"
        else:
            # self.safety-self.Stock
            return f"Refill-{self.safety-stock}"
          
class Stock_In(models.Model):
    supplier = models.ForeignKey(Supplier,verbose_name="Supplier", related_name='Stock_In_Supplier', on_delete=models.PROTECT,)
    location = models.ForeignKey(WHSBranch,verbose_name="Location", related_name='Stock_In_location', on_delete=models.PROTECT,)
    created=models.DateTimeField(("Created"),auto_now=True)
    updated=models.DateTimeField(("Updated"),auto_now_add=True)
    note = models.CharField("Note",max_length=50, null=True,blank=True)
    def __str__(self):
        return f"TR-IN--{self.id}"
    class Meta:
        verbose_name_plural = "STOCK_IN"
    
    def Items(self):
        total = 0
        items = self.Stock_IN_Detail.all()
        for item in items:
            total +=1
        return total
    
class Stock_IN_Detail(models.Model):
    stock_in = models.ForeignKey(Stock_In,verbose_name="Transaction_No", related_name='Stock_IN_Detail', on_delete=models.PROTECT,)
    item = models.ForeignKey(Item,verbose_name="Item", related_name='Stock_IN_Detail_item', on_delete=models.PROTECT,)
    quantity=models.IntegerField(("Quantity"),default=0)
    serial = models.CharField('Serial',max_length=50,null=True,blank=True,default="None")
    created=models.DateTimeField(("Created"),auto_now=True)
    updated=models.DateTimeField(("Updated"),auto_now_add=True)
    note = models.CharField("Note",max_length=50, null=True,blank=True)
    def __str__(self):
        return f"TR-IN--{self.stock_in.id}"
    
    class Meta:
        verbose_name_plural = "STOCK_IN_REF"
    
    
class Stock_Out(models.Model):
    customer = models.ForeignKey(Customer,verbose_name="Customer", related_name='Stock_Out_Customer', on_delete=models.PROTECT,null=True,blank=True)
    location = models.ForeignKey(WHSBranch,verbose_name="Location", related_name='Stock_Out_location', on_delete=models.PROTECT,)
    created=models.DateTimeField(("Created"),auto_now=True)
    updated=models.DateTimeField(("Updated"),auto_now_add=True)
    note = models.CharField("Note",max_length=50, null=True,blank=True)
    def __str__(self):
        return f"TR-OUT--{self.id}"
    class Meta:
        verbose_name_plural = "STOCK_OUT"
        
    def Items(self):
        total = 0
        items = self.Stock_Out_Detail.all()
        for item in items:
            total +=1
        return total
        
class Stock_Out_Detail(models.Model):
    stock_out = models.ForeignKey(Stock_Out,verbose_name="Transaction_No", related_name='Stock_Out_Detail', on_delete=models.PROTECT,)
    item = models.ForeignKey(Item,verbose_name="Item", related_name='Stock_Out_Detail_item', on_delete=models.PROTECT,)
    quantity=models.IntegerField(("Quantity"),default=0)
    serial = models.CharField('Serial',max_length=50,null=True,blank=True,default="None")
    created=models.DateTimeField(("Created"),auto_now=True)
    updated=models.DateTimeField(("Updated"),auto_now_add=True)
    note = models.CharField("Note",max_length=50, null=True,blank=True)
    def __str__(self):
        return f"TR-OUT--{self.stock_out.id}"
    class Meta:
        verbose_name_plural = "STOCK_OUT_REF"
    

# class Sales_Order(models.Model):
#     customer = models.ForeignKey(Customer,verbose_name="Customer", related_name='Sales_Order_Customer', on_delete=models.PROTECT,)
#     created=models.DateTimeField(("Created"),auto_now=True)
#     updated=models.DateTimeField(("Updated"),auto_now_add=True)
#     note = models.CharField("Note",max_length=50, null=True,blank=True)
#     def __str__(self):
#         return str(self.customer)
#     class Meta:
#         verbose_name_plural = "SALES_ORDER"
    
# class Sales_Order_Detail(models.Model):
#     sales_order = models.ForeignKey(Sales_Order,verbose_name="Sales_Order", related_name='Sales_Order_detail', on_delete=models.PROTECT,)
#     item = models.ForeignKey(Item,verbose_name="Item", related_name='Sales_Order_item', on_delete=models.PROTECT,)
#     quantity=models.IntegerField(("Quantity"),default=0)
#     serial = models.CharField('Serial',max_length=50,null=True,blank=True)
#     price=models.DecimalField(("Price"), max_digits=8, decimal_places=2,default=0)
#     discount=models.IntegerField(("Discount"),default=0)
#     created=models.DateTimeField(("Created"),auto_now=True)
#     updated=models.DateTimeField(("Updated"),auto_now_add=True)
#     note = models.CharField("Note",max_length=50, null=True,blank=True)
#     def __str__(self):
#         return str(self.sales_order.customer)
#     class Meta:
#         verbose_name_plural = "Sales_Order_Detail"
    
    

    

