from django.shortcuts import render, redirect
from .forms import ClothingForm, ClothingSearchForm, OutfitForm, OutfitSearchForm
from .models import Clothing, CATEGORY_CHOICES, Outfit
from django.contrib.auth.decorators import login_required
import codecs
from django.db.models import Q

def view_clothing(request):
    user = request.user
    query = request.GET.get('q')
    category = request.GET.get('category')  # Get the category from the URL parameter 'category'
    sort = request.GET.get('sort')  # Get the sort option from the URL parameter 'sort'
    clothing = Clothing.objects.filter(user=user)
    if query:
        clothing = clothing.filter(name__icontains=query)
    if category:
        clothing = clothing.filter(category=category)
    if sort == 'oldest':
        clothing = clothing.order_by('created_at')
    elif sort == 'newest':
        clothing = clothing.order_by('-created_at')
    return render(request, 'wardrobe/view_clothing.html', {'clothing': clothing})

def view_outfit(request):
    user = request.user
    query = request.GET.get('q')
    category = request.GET.get('category')  # Get the category from the URL parameter 'category'
    sort = request.GET.get('sort')  # Get the sort option from the URL parameter 'sort'
    outfit = Outfit.objects.filter(user=user)
    if query:
        outfit = outfit.filter(name__icontains=query)
    if category:
        outfit = outfit.filter(category__iexact=category)  # Use case-insensitive comparison with 'iexact'
    if sort == 'oldest':
        outfit = outfit.order_by('created_at')
    elif sort == 'newest':
        outfit = outfit.order_by('-created_at')
    return render(request, 'wardrobe/view_outfit.html', {'outfit': outfit})

def add_clothing(request):
    if request.method == 'POST':
        form = ClothingForm(request.POST, request.FILES)
        if form.is_valid():
            clothing = form.save(commit=False)
            clothing.user = request.user
            clothing.save()
            return redirect('view_clothing')
    else:
        form = ClothingForm()
    return render(request, 'wardrobe/add_clothing.html', {'form': form})

def add_outfit(request):
    if request.method == 'POST':
        form = OutfitForm(request.POST, request.FILES)
        if form.is_valid():
            outfit = form.save(commit=False)
            outfit.user = request.user
            outfit.save()
            return redirect('view_outfit')
    else:
        form = OutfitForm()
    return render(request, 'wardrobe/add_outfit.html', {'form': form})    

def delete_clothing(request):
    if request.method == 'POST':
        clothing_ids = request.POST.getlist('clothing')
        Clothing.objects.filter(id__in=clothing_ids).delete()     
    return redirect('view_clothing')

def delete_outfit(request):
    if request.method == 'POST':
        outfit_ids = request.POST.getlist('outfit')
        Outfit.objects.filter(id__in=outfit_ids).delete()
    return redirect('view_outfit')

def test(request):
    return render(request, 'wardrobe/test.html')

def about(request):
    return render(request, 'about.html')

