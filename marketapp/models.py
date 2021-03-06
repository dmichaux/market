from django.db import models

class User(models.Model):
    name  = models.CharField(max_length=100)
    city  = models.CharField(max_length=50)
    state = models.CharField(max_length=2)
    join_date     = models.DateTimeField()
    items_sold    = models.PositiveIntegerField(default=0)
    items_baught  = models.PositiveIntegerField(default=0)
    success_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

    def full_location(self):
        return f"{self.city}, {self.state}"
    
    def total_transactions(self):
        return self.items_sold + self.items_baught
  
    def success_rate(self):
        rate = 0
        color = 'red'
        transactions = self.total_transactions()
        if transactions > 0:
            rate = (self.success_count / transactions) * 100
        if rate > 70:
            color = 'green'
        return {'rate': rate, 'color': color}

class Category(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

class Item(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                           related_name="items")
    seller   = models.ForeignKey(User, on_delete=models.CASCADE,
                                       related_name="items")
    name   = models.CharField(max_length=100)
    price  = models.PositiveIntegerField(default=20)
    baught = models.BooleanField(default=False)
    baught_date = models.DateTimeField(null=True)
    description = models.CharField(max_length=150)
    list_date   = models.DateTimeField()

    def __str__(self):
        return self.name

class Message(models.Model):
    sender    = models.ForeignKey(User, on_delete=models.CASCADE,
                                        related_name='messages_sent')
    recipient = models.ForeignKey(User, on_delete=models.CASCADE,
                                        related_name='messages_received')
    subject   = models.ForeignKey(Item, on_delete=models.CASCADE,
                                        related_name='messages')
    text    = models.TextField(max_length=200)
    sent_at = models.DateTimeField()

    def __str__(self):
        return f"From: {self.sender}, To: {self.recipient}, Sent: {self.sent_at}"
