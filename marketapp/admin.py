from django.contrib import admin
from .models import User, Category, Item, Message

admin_models = [
    User,
    Category,
    Item,
    Message
]

admin.site.register(admin_models)
