from rest_framework import serializers
from .models import *



class Voice_CommandSerializer(serializers.ModelSerializer):
    item= serializers.StringRelatedField()

    class Meta:
        model = Voice_Command
        fields= ["action_name","action_state","command",'item',]
        # exclude = ('id',)

class ADSerializer(serializers.ModelSerializer):
    class Meta:
        model = AD
        fields= ['title',"message","ad_url","image","video"]
        # exclude = ('id',)

class ComplaintSerializer(serializers.ModelSerializer):
    item= serializers.StringRelatedField()
    class Meta:
        model = Complaint
        fields= ['title',"content","status","customer","item"]
        # exclude = ('id',)

class Actionesrializer(serializers.ModelSerializer):
    item= serializers.StringRelatedField()
    class Meta:
        model = Action
        fields= ["state","value","item"]
        # exclude = ('id',)

class UpdateSerializer(serializers.ModelSerializer):
    product= serializers.StringRelatedField()
    class Meta:
        model = Update
        fields= ["last_version_number","last_version_url",'product']
        # exclude = ('id',)



class ItemSerializer(serializers.ModelSerializer):
    products= serializers.StringRelatedField()
    users_list= serializers.StringRelatedField()
    room = serializers.StringRelatedField()
    voice_command=Voice_CommandSerializer(source='Item_Voice_Command',many=True)
    Complaint=ComplaintSerializer(source='Item_Complaint',many=True)
    Actions = Actionesrializer(source='Item_Action',many=True) 
    # update=UpdateSerializer(source='Item_Complaint',many=True)

    class Meta:
        model = Item
        fields= ["device_name","item_mac_ip","is_assigned","last_version","do_update_now",'products',"users_list","room","voice_command","Complaint","Actions"]
        # exclude = ('id',)

class ProductSerializer(serializers.ModelSerializer):
    Update = UpdateSerializer(source='Product_Update',many=True)
    items = ItemSerializer(source='Product_Items',many=True)
    class Meta:
        model = Product
        fields= ['name',"electricity_consumption","image_url","last_version_number","last_version_url","items","Update"]
        # exclude = ('id',)

class RoomSerializer(serializers.ModelSerializer):
    item= ItemSerializer(source='Room_Item',many=True)
    class Meta:
        model = Room
        fields= ['title',"image_url","item"]
        # exclude = ('id',)

class CustomUserSerializer(serializers.ModelSerializer):
    # user = serializers.StringRelatedField()
    items=ItemSerializer(source='User_Item',many=True)
    Complaint=ComplaintSerializer(source='Customer_Complaint',many=True)

    class Meta:
        model = CustomUser
        fields= ['username',"phone","email","password","image","items","Complaint"]
        # exclude = ('id',)

