#items/urls.py
from django.urls import path
from items import views

urlpatterns = [
    path('api/items/', views.create_item, name='create_item'),  # Create Item function-based view
    path('api/items/<int:item_id>/', views.read_item, name='read_item'),  # Read, update, and delete
]
