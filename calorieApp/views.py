
from django.shortcuts import render, redirect
from .models import FoodItem
from django.db.models import Sum

# Create your views here.

def index(request):
    items = FoodItem.objects.all()
    total_calories = items.aggregate(Sum('calories'))['calories__sum'] or 0
    
    if request.method == 'POST':
        # Logic to add a new item
        name = request.POST.get('name')
        calories = request.POST.get('calories')
        FoodItem.objects.create(name=name, calories=calories)
        return redirect('/')
        
    return render(request, 'index.html', {'items': items, 'total': total_calories})