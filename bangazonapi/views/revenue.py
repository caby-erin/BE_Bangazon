from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from bangazonapi.models import Revenue, Order, OrderItem

class RevenueView(ViewSet):
  def retrieve(self, request, pk):
    revenue = Revenue.objects.get(pk=pk)
    serializer = RevenueSerializer(revenue)
    return Response(serializer.data)
  
  def list(self, request):
    revenues = Revenue.objects.all()
    serializer = RevenueSerializer(revenues, many=True)
    return Response(serializer.data)
  
  def create(self, request):
    serializer = RevenueSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # total_order_amount = 0
    # order = Order.objects.get(id=request.data["order"])
    # order_items = OrderItem.objects.filter(order=order)
    
    # for order_item in order_items:
    #   total_order_amount += order_item.item.price
    
    # revenue = Revenue.objects.create(
    #   payment_type=request.data["paymentType"],
    #   tip_amount=request.data["tipAmount"],
    #   order=order,
    #   totalOrderAmount = total_order_amount,
    # )
    # serializer = RevenueSerializer(revenue)
    # return Response(serializer.data)

class RevenueSerializer(serializers.ModelSerializer):
  class Meta:
    model = Revenue
    fields = ('id', 'order', 'total_order_amount', 'tip_amount', 'payment_type', 'date')
