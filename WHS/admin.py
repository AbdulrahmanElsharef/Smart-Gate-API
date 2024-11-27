from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin

# Register your models here.
@admin.register(Item)
class ItemsAdmin(ImportExportModelAdmin):
    list_display =['id','sku','name','uom','color','brand','category','Total_In','Total_out','Stock',"safety",'Status',]
    list_filter =['id','sku','name','uom__name','color__name','brand__name','category__name','created']
    exclude=("created","updated")

class Stock_IN_Detail_TabularInline(admin.TabularInline):
     model = Stock_IN_Detail
     extra = 0

class Stock_Out_Detail_TabularInline(admin.TabularInline):
     model = Stock_Out_Detail
     extra = 0


@admin.register(Stock_In)
class Stock_In_Admin(ImportExportModelAdmin):
    inlines = [Stock_IN_Detail_TabularInline]
    list_display =['__str__','location','supplier','Items','note','created']
    list_filter =['id','location__name','supplier__name','created']
    
@admin.register(Stock_IN_Detail)
class Stock_IN_Detail_Admin(ImportExportModelAdmin):
    list_display =['__str__','supplier_','location_','item','sku_','serial','name_',"color_","brand_",'category_','UOM_','Quantity_',]
    list_filter =['stock_in__id','stock_in__supplier__name','stock_in__location__name','item','item__sku','serial','item__name','item__color__name','item__brand__name','item__category__name','item__uom__name','created']
    

    def supplier_(self, obj):
        return obj.stock_in.supplier
    def location_(self, obj):
        return obj.stock_in.location 
    def Quantity_(self, obj):
        return obj.quantity
    def UOM_(self, obj):
        return obj.item.uom 
    def sku_(self, obj):
        return obj.item.sku 
    def name_(self, obj):
        return obj.item.name 
    def color_(self, obj):
        return obj.item.color 
    def brand_(self, obj):
        return obj.item.brand 
    def category_(self, obj):
        return obj.item.category 
    def safety_(self, obj):
        return obj.item.safety 
    def Stock_(self, obj):
        stock=obj.item.Stock() 
        return stock
    def Status_(self, obj):
        stock=obj.item.Status() 
        return stock

    
@admin.register(Stock_Out)
class Stock_Out_Admin(ImportExportModelAdmin):
    inlines = [Stock_Out_Detail_TabularInline]
    list_display =['__str__','location','customer','Items','note','created']
    list_filter =['id','location__name','customer__name','created']
    
@admin.register(Stock_Out_Detail)
class Stock_Out_Detail_Admin(ImportExportModelAdmin):
    list_display =['__str__','customer_','location_','item','sku_','serial','name_',"color_","brand_",'category_','UOM_','Quantity_']
    list_filter =['stock_out__id','stock_out__customer__name','stock_out__location__name','item','item__sku','serial','item__name','item__color__name','item__brand__name','item__category__name','item__uom__name','created']
    

    def customer_(self, obj):
        return obj.stock_out.customer
    def location_(self, obj):
        return obj.stock_out.location 
    def Quantity_(self, obj):
        return obj.quantity
    def UOM_(self, obj):
        return obj.item.uom 
    def sku_(self, obj):
        return obj.item.sku 
    def name_(self, obj):
        return obj.item.name 
    def color_(self, obj):
        return obj.item.color 
    def brand_(self, obj):
        return obj.item.brand 
    def category_(self, obj):
        return obj.item.category 
    def safety_(self, obj):
        return obj.item.safety 
    def Stock_(self, obj):
        stock=obj.item.Stock() 
        return stock
    def Status_(self, obj):
        stock=obj.item.Status() 
        return stock