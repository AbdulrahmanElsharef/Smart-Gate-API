from rest_framework import generics
from .serializer import *
from.models import *

class Voice_Command_List_API(generics.ListCreateAPIView):
    serializer_class = Voice_CommandSerializer
    queryset = Voice_Command.objects.all()
class Voice_Command_Detail_API(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = Voice_CommandSerializer
    queryset = Voice_Command.objects.all()
    lookup_field = 'slug'

class AD_List_API(generics.ListCreateAPIView):
    serializer_class = ADSerializer
    queryset = AD.objects.all()
class AD_Detail_API(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ADSerializer
    queryset = AD.objects.all()
    lookup_field = 'slug'

class Complaint_List_API(generics.ListCreateAPIView):
    serializer_class = ComplaintSerializer
    queryset = Complaint.objects.all()
class Complaint_Detail_API(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ComplaintSerializer
    queryset = Complaint.objects.all()
    lookup_field = 'slug'

class Action_List_API(generics.ListCreateAPIView):
    serializer_class = Actionesrializer
    queryset = Product_Action.objects.all()
class Action_Detail_API(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = Actionesrializer
    queryset = Product_Action.objects.all()
    lookup_field = 'slug'

class Update_List_API(generics.ListCreateAPIView):
    serializer_class = UpdateSerializer
    queryset = Update.objects.all()
class Update_Detail_API(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UpdateSerializer
    queryset = Update.objects.all()
    lookup_field = 'slug'

class Item_List_API(generics.ListCreateAPIView):
    serializer_class = ItemSerializer
    queryset = Item.objects.all()
class Item_Detail_API(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ItemSerializer
    queryset = Item.objects.all()
    lookup_field = 'slug'

class Product_List_API(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
class Product_Detail_API(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    lookup_field = 'slug'
    
class Room_List_API(generics.ListCreateAPIView):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()
class Room_Detail_API(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()
    lookup_field = 'slug'

class CustomUser_List_API(generics.ListCreateAPIView):
    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.all()
class CustomUser_Detail_API(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.all()
    lookup_field = 'slug'