from django.contrib import admin
from .models import *
from WHS.models import *
# Register your models here.

class ItemTabularInline(admin.TabularInline):
     model = Item
     extra = 0
class SubCategoryTabularInline(admin.TabularInline):
     model = SubCategory
     extra = 0
class CategoryTabularInline(admin.TabularInline):
     model = Category
     extra = 0
class Stock_In_TabularInline(admin.TabularInline):
     model = Stock_In
     extra = 0
class Stock_Out_TabularInline(admin.TabularInline):
     model = Stock_Out
     extra = 0
class Stock_IN_Detail_TabularInline(admin.TabularInline):
     model = Stock_IN_Detail
     extra = 0
class Stock_Out_Detail_TabularInline(admin.TabularInline):
     model = Stock_Out_Detail
     extra = 0


@admin.register(UOM)
class UOMAdmin(admin.ModelAdmin):
    list_display =["name",'created']
    list_filter=["name",'created']
    
@admin.register(WHSBranch)
class WHSBranchAdmin(admin.ModelAdmin):
    # inlines = [Stock_IN_Detail_TabularInline,Stock_Out_Detail_TabularInline]
    list_display =["name",'detail','created']
    list_filter=["name",'created']
    

@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display =["name",'created']
    list_filter=["name",'created']
    
@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    inlines = [ItemTabularInline]
    list_display =["name",'created']
    list_filter=["name",'created']
    
@admin.register(MainCategory)
class MainCategoryAdmin(admin.ModelAdmin):
    inlines = [SubCategoryTabularInline]
    list_display =["name",'created']
    list_filter=["name",'created']
    
@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    inlines = [CategoryTabularInline]
    list_display =["name",'main','created']
    list_filter=["name",'main','created']
    
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = [ItemTabularInline]
    list_display =["name",'sub_category','created']
    list_filter=["name",'sub_category','created']
    
@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    inlines = [Stock_In_TabularInline]
    list_display =["name",'phone','created']
    list_display =["name",'phone','created'] 
       
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    inlines = [Stock_Out_TabularInline]
    list_display =["name",'phone','created']
    list_display =["name",'phone','created'] 
