from django.shortcuts import render, redirect
from .forms import CategoryForm, PageForm
# Create your views here.
from rango.models import Category, Page


def index(request):
    category_list = Category.objects.order_by('-likes')[:5]
    return render(request, 'rango/index.html', {'categories': category_list})


def category(request, category_id):
    context_dict = {}

    try:
        category = Category.objects.get(pk=category_id)
        context_dict['category_name'] = category.name
        pages = Page.objects.filter(category=category)
        context_dict['pages'] = pages
        context_dict['category'] = category
    except Category.DoesNotExist:
        pass
    return render(request, 'rango/category.html', context_dict)


def add_category(request):
    if request.POST:
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)  # redirect to index
        else:
            print(form.errors)  # maybe show again the errors and the form
    else:
        # GET here
        form = CategoryForm()
    # GET here
    return render(request, 'rango/add_category.html', {'form': form})


def add_page(request, category_id):
    try:
        category = Category.objects.get(pk=category_id)
    except Category.DoesNotExist:
        category = None

    if request.POST:
        form = PageForm(request.POST)
        if form.is_valid() and category:
            page = form.save(commit=False)
            page.category = category
            page.views = 0
            page.save()
            return redirect('rango/category.html', {'category_id': category_id})
        else:
            print(form.errors)
    else:
        form = PageForm()

    context_dict = {'form': form, 'category': category}
    return render(request, 'rango/add_page.html', context_dict)
