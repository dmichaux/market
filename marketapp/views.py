import random
from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from .models import User, Category, Item

def home(request):
    # Home page with sign-up/in, my page link, search form, featured items
    categorized_items = []
    categories = random.sample(set(Category.objects.all()), 6)
    for category in categories:
        items = random.sample(set(category.items.all()), 2)
        details = {'category': category.name,
                   'items': items}
        categorized_items.append(details)
    context = {'categorized_items': categorized_items}
    return render(request, './home.html', context)

def index(request):
    # List, search, filter(price, category, list_date, etc.)
    master_list = Item.objects.all()
    paginator = Paginator(master_list, 15)
    page = request.GET.get('page')
    items = paginator.get_page(page)
    context = {'items': items}
    return render(request, 'items/index.html', context)

def detail(request, item_id):
    # Details on item, form to message about it
    item = get_object_or_404(Item, pk=item_id)
    context = {'item': item}
    return render(request, 'items/detail.html', context)

def user_page(request, user_id):
    # User info, messages, listed items, favorited items?
    user = get_object_or_404(User, pk=user_id)
    context = {'user': user}
    return render(request, 'users/user_page.html', context)
