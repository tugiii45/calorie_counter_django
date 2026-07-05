from django.shortcuts import render, redirect
from .models import FoodItem
from django.db.models import Sum

def index(request):
    if request.method == 'POST':
        # Add a new food item
        if 'add' in request.POST:
            name = request.POST.get('name')
            calories = request.POST.get('calories')
            FoodItem.objects.create(name=name, calories=calories)
        
        # Reset all items
        elif 'reset' in request.POST:
            FoodItem.objects.all().delete()
            
        # Remove a specific item
        elif 'delete' in request.POST:
            item_id = request.POST.get('item_id')
            FoodItem.objects.filter(id=item_id).delete()
            
        return redirect('/')

    # GET request: Display items and total
    items = FoodItem.objects.all()
    total = items.aggregate(Sum('calories'))['calories__sum'] or 0
    return render(request, 'index.html', {'items': items, 'total': total})