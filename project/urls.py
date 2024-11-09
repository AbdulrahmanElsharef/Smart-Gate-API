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

urlpatterns = [
    path('admin/', admin.site.urls),

    path('Command/list', Voice_Command_List_API.as_view()),
    path('Command/list/<str:id>', Voice_Command_Detail_API.as_view()),

    path('ad/list', AD_List_API.as_view()),
    path('ad/list/<str:id>', AD_Detail_API.as_view()),

    path('complaint/list', Complaint_List_API.as_view()),
    path('complaint/list/<int:id>', Complaint_Detail_API.as_view()),

    path('action/list', Action_List_API.as_view()),
    path('action/list/<str:id>', Action_Detail_API.as_view()),

    path('items', Items_API.as_view()),
    path('items/<str:id>', Item_Detail_API.as_view()),
    path('listitems', Item_list_API.as_view()),

    path('products', Products_API.as_view()),
    path('products/<str:id>', Product_Detail_API.as_view()),

    path('listproducts', ListProductApi.as_view()),

    path('room/list', Room_List_API.as_view()),
    path('room/list/<str:id>', Room_Detail_API.as_view()),

    path('user/list', CustomUser_List_API.as_view()),
    path('user/list/<str:id>', CustomUser_Detail_API.as_view()),



]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
