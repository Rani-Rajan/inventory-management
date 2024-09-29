#items/views.py
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Item
from .serializers import ItemSerializer

# Class-Based Views for List and Create
class ItemListCreateView(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

# Class-Based Views for Retrieve, Update, and Destroy
class ItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

@api_view(['POST'])
def create_item(request):
    serializer = ItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_item(request, item_id):
    try:
        item = Item.objects.get(pk=item_id)
    except Item.DoesNotExist:
        return Response({'error': 'Item not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = ItemSerializer(item, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_item(request, item_id):
    try:
        item = Item.objects.get(pk=item_id)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)  # Return 204 No Content on successful deletion
    except Item.DoesNotExist:
        return Response({'error': 'Item not found'}, status=status.HTTP_404_NOT_FOUND)
        
# Handle Read, Update, and Delete in a function-based view (if still required)
@api_view(['GET', 'PUT', 'DELETE'])
def read_item(request, item_id):
    try:
        item = Item.objects.get(pk=item_id)
    except Item.DoesNotExist:
        return Response({'error': 'Item not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        # Read Item
        serializer = ItemSerializer(item)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        # Update Item
        serializer = ItemSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        # Delete Item
        item.delete()
        return Response({'message': 'Item deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
