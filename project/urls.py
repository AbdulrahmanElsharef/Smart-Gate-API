"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from Product.api import *
from WHS import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('stock_in/', views.stock_in_all,name='stock_in_all'),
    path('stock_in/<int:id>', views.stock_in_detail,name="stock_in"),
    path('stock_out/', views.stock_out_all,name='stock_out_all'),
    path('stock_out/<int:id>', views.stock_out_detail,name="stock_out"),

    # path('test', Test_List_API.as_view()),
    # path('test/<int:id>', Test_Detail_API.as_view()),

    # path('list/Command', Voice_Command_List_API.as_view()),
    # path('list/Command/<str:id>', Voice_Command_Detail_API.as_view()),

    # path('list/ad', AD_List_API.as_view()),
    # path('list/ad/<str:id>', AD_Detail_API.as_view()),

    # path('list/complaint', Complaint_List_API.as_view()),
    # path('list/complain/<int:id>', Complaint_Detail_API.as_view()),

    # path('list/action', Action_List_API.as_view()),
    # path('list/action/<str:id>', Action_Detail_API.as_view()),

    # path('list/items', Item_list_API.as_view()),
    # path('list/item', Items_API.as_view()),
    # path('list/item/<str:id>', Item_Detail_API.as_view()),

    # path('list/products', ListProductApi.as_view()),
    # path('list/product', Products_API.as_view()),
    # path('list/product/<str:id>', Product_Detail_API.as_view()),


    # path('room/list', Room_List_API.as_view()),
    # path('room/list/<str:id>', Room_Detail_API.as_view()),

    # path('list/users', ListUserApi.as_view()),
    # path('list/user', CustomUser_List_API.as_view()),
    # path('list/user/<str:id>', CustomUser_Detail_API.as_view()),

]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
