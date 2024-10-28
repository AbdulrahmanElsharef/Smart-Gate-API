# from rest_framework import serializers
# from .models import *



# class Voice_CommandSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Voice_Command
#         fields= '__all__'
# class ADSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = AD
#         fields= '__all__'
# class ComplaintSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Complaint
#         fields= '__all__'
# class Actionesrializer(serializers.ModelSerializer):
#     class Meta:
#         model = Action
#         fields= '__all__'
# class UpdateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Update
#         fields= '__all__'



# class ItemSerializer(serializers.ModelSerializer):
#     products= serializers.StringRelatedField()
#     users_list= serializers.StringRelatedField()
#     room = serializers.StringRelatedField()
#     voice_command=Voice_CommandSerializer(source='Item_Voice_Command',many=True)
#     Complaint=ComplaintSerializer(source='Item_Complaint',many=True)
#     Actions = Actionesrializer(source='Item_Action',many=True) 
#     # update=UpdateSerializer(source='Item_Complaint',many=True)

#     class Meta:
#         model = Item
#         fields= '__all__'

# class ProductSerializer(serializers.ModelSerializer):
#     Update = UpdateSerializer(source='Product_Update',many=True)
#     items = ItemSerializer(source='Product_Items',many=True)
#     class Meta:
#         model = Product
#         fields= '__all__'

# class RoomSerializer(serializers.ModelSerializer):
#     item= ItemSerializer(source='Room_Item',many=True)
#     class Meta:
#         model = Room
#         fields= '__all__'

# class CustomUserSerializer(serializers.ModelSerializer):
#     user = serializers.StringRelatedField()
#     items=ItemSerializer(source='used_item',many=True)
#     Complaint=ComplaintSerializer(source='Customer_Complaint',many=True)

#     class Meta:
#         model = CustomUser
#         fields= '__all__'


