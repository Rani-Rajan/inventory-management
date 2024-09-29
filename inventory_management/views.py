# inventory_management/views.py
from django.shortcuts import render, redirect
from items.models import Item
from items.forms import ItemForm

def create_item(request):
    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('item_list')  # Redirect to the item list or another view
    else:
        form = ItemForm()
    return render(request, 'create_item.html', {'form': form})

# Additional views for reading, updating, and deleting items can be added similarly if needed.
