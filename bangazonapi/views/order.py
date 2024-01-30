from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from bangazonapi.models import Order, User, Item, OrderItem
from rest_framework.decorators import action

class OrderView(ViewSet):
  # @action(methods=['post'], detail=True)
  # def add_item_to_order(self, request, pk):
  #   '''post request for a user to add an item to an order'''
  #   order = Order.objects.get(pk=pk)
  #   item = Item.objects.get(pk=request.data['item'])
  #   orderitem = OrderItem.objects.create(
  #     item=item,
  #     order=order
  #   )
  #   return Response(status=status.HTTP_201_CREATED)
  
  
  # @action(methods=['delete'], detail=True)
  # def remove_item_from_order(self, request, pk):
  #   '''Delete request for a user to remove an item from an order'''
  #   orderitem = request.data.get("order_item")
  #   OrderItem.objects.filter(pk=orderitem, order__pk=pk).delete()
  #   return Response(status=status.HTTP_204_NO_CONTENT)
    
    
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
  
  @action(detail=True, methods=['PATCH'])
  def close_order(self, request, pk=None):
    order = Order.objects.get(pk=pk)
    order.is_closed = True
    order.save()
    return Response({'status': 'order closed'}, status=status.HTTP_200_OK)
  
class OrderItemSerializer(serializers.ModelSerializer):
  price = serializers.ReadOnlyField(source='item.price')
  name = serializers.ReadOnlyField(source='item.name')
  class Meta:
    model = OrderItem
    fields = ('id', 'price', 'name')
  
class OrderSerializer(serializers.ModelSerializer):
  items = OrderItemSerializer(many=True, read_only=True)
  class Meta:
    model = Order
    fields = ('id', 'user', 'name', 'is_closed', 'customer_phone', 'customer_email', 'order_type', 'items')
    depth = 1
