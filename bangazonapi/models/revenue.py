from django.db import models
from django.db.models import Count, Sum
from .order import Order

class Revenue(models.Model):
  order = models.ForeignKey(Order, on_delete=models.CASCADE)
  total_order_amount = models.DecimalField(max_digits=7, decimal_places=2)
  date = models.DateField(auto_now=True)
  payment_type = models.CharField(max_length=50)
  tip_amount = models.DecimalField(max_digits=7, decimal_places=2)
  
  @property
  def total_tips(self):
      tips = Revenue.objects.aggregate(tip_total=Sum('tip_amount')) ['tip_total']
      return tips
    
