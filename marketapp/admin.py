from django.contrib import admin
from .models import User, Item, Message

admin_models = [
  User,
  Item,
  Message
]

admin.site.register(admin_models)
