from django import forms
from .models import CATEGORY_CHOICES, Clothing , Outfit

class ClothingForm(forms.ModelForm):
    category = forms.ChoiceField(choices=CATEGORY_CHOICES)

    class Meta:
        model = Clothing
        fields = ['name', 'category', 'image']

class ClothingSearchForm(forms.Form):
    search_query = forms.CharField(label='Search')

class OutfitForm(forms.ModelForm):
    class Meta:
        model = Outfit
        fields = ['name', 'category', 'image']

class OutfitSearchForm(forms.Form):
    search_query = forms.CharField(label='Search')

