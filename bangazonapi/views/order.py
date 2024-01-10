from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from bangazonapi.models import Order, User

class OrderView(ViewSet):
  def retrieve(self, request, pk):
    order = Order.objects.get(pk=pk)
    serializer = OrderSerializer(order)
    return Response(serializer.data)
  
  def list(self, request):
    orders = Order.objects.all()
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
  
  def create(self, request):
    user = User.objects.get(pk=request.data["user"])
    
    order = Order.objects.create(
      user = user,
      name=request.data["name"],
      is_closed=request.data["isClosed"],
      customer_phone=request.data["customerPhone"],
      customer_email=request.data["customerEmail"],
      order_type=request.data["orderType"]
    )
    
    order.save()
    serializer = OrderSerializer(order)
    return Response(serializer.data)
  
  def update(self, request, pk):
    order = Order.objects.get(pk=pk)
    order.name=request.data["name"]
    order.is_closed=request.data["isClosed"]
    order.customer_phone=request.data["customerPhone"]
    order.customer_email=request.data["customerEmail"]
    order.order_type=request.data["orderType"]
    
    order.save()
    return Response(None, status=status.HTTP_200_OK)
  
  def destroy(self, request, pk):
    order = Order.objects.get(pk=pk)
    order.delete()
    return Response(None, status=status.HTTP_204_NO_CONTENT)
  
class OrderSerializer(serializers.ModelSerializer):
  class Meta:
    model = Order
    fields = ('id', 'user', 'name', 'is_closed', 'customer_phone', 'customer_email', 'order_type')
