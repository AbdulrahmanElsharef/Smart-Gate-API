# from django.contrib import admin
# from .models import *

# # Register your models here.
# # class YourModelAdmin(admin.ModelAdmin):
# #     list_display = [field.name for field in YourModel._meta.fields]

# class ActionTabularInline(admin.TabularInline):
#      model = Action
#      extra = 0

# class UpdateTabularInline(admin.TabularInline):
#      model = Update
#      extra = 0
# class Voice_CommandTabularInline(admin.TabularInline):
#      model = Voice_Command
#      extra = 0

# @admin.register(CustomUser)
# class CustomUserAdmin(admin.ModelAdmin):
#     list_display =[field.name for field in CustomUser._meta.fields]
# @admin.register(Room)
# class RoomAdmin(admin.ModelAdmin):
#     list_display =[field.name for field in Room._meta.fields]
# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     inlines = [ActionTabularInline,UpdateTabularInline]  
#     list_display =[field.name for field in Product._meta.fields]
# @admin.register(Item)
# class ItemsAdmin(admin.ModelAdmin):
#     inlines = [Voice_CommandTabularInline]  
#     list_display =[field.name for field in Item._meta.fields]
# @admin.register(AD)
# class ADAdmin(admin.ModelAdmin):
#     list_display =[field.name for field in AD._meta.fields]
# @admin.register(Complaint)
# class ComplaintAdmin(admin.ModelAdmin):
#     list_display =[field.name for field in Complaint._meta.fields]
