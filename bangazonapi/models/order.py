from django.db import models
from .user import User

class Order(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
  name = models.CharField(max_length=50)
  is_closed = models.BooleanField()
  customer_phone = models.CharField(max_length=50)
  customer_email = models.CharField(max_length=50)
  order_type = models.CharField(max_length=50)
  
