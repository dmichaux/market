from django.shortcuts import render, get_object_or_404

from .models import User, Item

def home(request):
  # Home page with sign-up/in, my page link, search form featured items
  return render(request, './home.html')

def index(request):
  # List, search, filter(price, category, list_date, etc.)
  master_list = Item.objects.all()
  context = {'master_list': master_list}
  return render(request, 'items/index.html', context)

def detail(request, item_id):
  # Details on item, form to message about it
  item = get_object_or_404(Item, pk = item_id)
  context = {'item': item}
  return render(request, 'items/detail.html', context)

def user_page(request, user_id):
  # User info, messages, listed items, favorited items?
  user = get_object_or_404(User, pk = user_id)
  context = {'user': user}
  return render(request, 'users/user_page.html', context)