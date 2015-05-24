from django import forms
from rango.models import Category, Page

class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text='Enter category name')

    class Meta:
        model = Category
        fields = ['name']
        exclude = ['likes']


class PageForm(forms.ModelForm):
    title = forms.CharField(max_length=100)
    url = forms.CharField(max_length=100)

    class Meta:
        model = Page
        fields = ['title', 'url']
        exclude = ['category']
