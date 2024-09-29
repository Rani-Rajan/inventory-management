"""
URL configuration for inventory_management project.

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
#inventory_management/urls.py
from django.contrib import admin  # This is the missing import
from django.urls import path, include
from items import views  # Import your API views

urlpatterns = [
    # API endpoints for items
    path('api/items/', views.create_item, name='create_item'),  # Create Item
    path('api/items/<int:item_id>/update/', views.update_item, name='update_item'),  # Update Item
    path('api/items/<int:item_id>/delete/', views.delete_item, name='delete_item'),  # Delete Item
    path('api/items/', views.ItemListCreateView.as_view(), name='item-list-create'),  # Create/List Items
    path('api/items/<int:item_id>/', views.read_item, name='read_item'),  # Read, Update, Delete Item
   
    # Admin and other paths
    path('admin/', admin.site.urls),  # Django Admin
    path('', include('items.urls')),
    # Add JWT token paths if you're using JWT authentication
]




