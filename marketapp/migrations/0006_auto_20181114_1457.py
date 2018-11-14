# Generated by Django 2.1.3 on 2018-11-14 19:57

from django.db import migrations
from django.utils import timezone
import random

def seed_items(apps, schema_editor):
  Category = apps.get_model('marketapp', 'Category')
  categories = Category.objects.all()
  User = apps.get_model('marketapp', 'User')
  users = User.objects.all()
  Item = apps.get_model('marketapp', 'Item')
  for user in users:
    for i in range(10):
      category = random.choice(categories)
      thing, price = map_thing_price(category.name)
      item = Item(name = thing, price = price,
                  category = category, seller = user,
                  description = f"I'm selling this {thing}. Good condition. Message for details!",
                  list_date = timezone.now())
      item.save()

class Migration(migrations.Migration):

    dependencies = [
        ('marketapp', '0005_auto_20181114_1446'),
    ]

    operations = [
      migrations.RunPython(seed_items),
    ]

def map_thing_price(category):
  switch = {
    'furniture': {
      'thing': ['chair', 'sofa', 'bed'],
      'price': [70, 100, 89]},
    'apparel': {
      'thing': ['coat', 'sweater', 'hoodie'],
      'price': [40, 35, 55]},
    'jewelry': {
      'thing': ['ring', 'watch', 'tie clip'],
      'price': [112, 185, 290]},
    'antique': {
      'thing': ['clock', 'record player', 'foot locker'],
      'price': [150, 95, 225]},
    'electronics': {
      'thing': ['PS4', 'TV', 'iPad'],
      'price': [280, 320, 450]},
    'cell phones': {
      'thing': ['iPhone', 'Galaxy', 'Nokia brickphone'],
      'price': [290, 315, 260]},
    'kitchen': {
      'thing': ['knife set', 'juicer', 'stand mixer'],
      'price': [60, 85, 40]},
    'automotive': {
      'thing': ['Mini Cooper', 'Honda Rebel 250', 'Toyota Prius'],
      'price': [4599, 3995, 3499]},
    'baby/kid goods': {
      'thing': ['crib', "box of toys", 'toddler bed'],
      'price': [160, 75, 100]},
    'outdoors': {
      'thing': ['tent', '70L backpack', 'stove'],
      'price': [250, 195, 115]},
    'collectible': {
      'thing': ['set of vinyl records', 'box of trading cards', 'lot of Pez dispensers'],
      'price': [85, 120, 60]},
    'hand crafted': {
      'thing': ['pottery mug', 'knitted scarf', 'case of homebrewed IPA'],
      'price': [50, 135, 80]},
    'books': {
      'thing': ['Tao Te Ching by Lao Tzu', 'Brave New World by Aldous Huxley',
                'What is Property? by Pierre-Joseph Proudhon'],
      'price': [10, 15]},
    'artwork': {
      'thing': ['painting', 'display of photo prints', 'mosaic'],
      'price': [375, 225, 200]}
  }
  selected = switch.get(category)
  thing = random.choice(selected['thing'])
  price = random.choice(selected['price'])
  return (thing, price)
