from django.shortcuts import render, redirect, get_object_or_404
from .models import Item
from .forms import ItemForm

def get_todo_list(request):
    results = Item.objects.all()
    return render(request, 'todo_list.html', {'items': results})

def create_an_item(request):
    if request.method == "POST":
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(get_todo_list)
    else:
        form = ItemForm()

    return render(request, 'item_form.html', {'form': form})

def edit_item(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    if request.method == "POST":
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect(get_todo_list)
    else:
        form = ItemForm(instance=item)
    return render(request, 'item_form.html', {'form': form})

def toggle_status(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    item.done = not item.done
    item.save()
    return redirect(get_todo_list)