from django.db import models

class User(models.Model):
  name = models.CharField(max_length = 100)
  city = models.CharField(max_length = 50)
  state = models.CharField(max_length = 2)
  join_date = models.DateTimeField('date joined')
  items_sold = models.PositiveIntegerField(default = 0)
  items_baught = models.PositiveIntegerField(default = 0)
  success_count = models.PositiveIntegerField(default = 0)

  def __str__(self):
    return self.name

  def full_location(self):
    return f"{self.city}, {self.state}"
  
  def success_rate(self):
    transactions = self.items_sold + self.items_baught
    rate = 0
    if transactions > 0:
      rate = (self.success_count / transactions) * 100
    return rate

class Item(models.Model):
  user = models.ForeignKey(User, on_delete = models.CASCADE)
  name = models.CharField(max_length = 100)
  category = models.CharField(max_length = 50)
  description = models.CharField(max_length = 150)
  price = models.PositiveIntegerField(default = 20)
  list_date = models.DateTimeField('date listed')
  baught = models.BooleanField(default = False)

  def __str__(self):
    return self.name
