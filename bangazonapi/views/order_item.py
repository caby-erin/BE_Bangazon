from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from bangazonapi.models import OrderItem, Order, Item

class OrderItemView(ViewSet):
  """Order Item View"""
  
  def retrieve(self, request, pk):
    """Handles GET request for single order item"""
    
    try:
      order_item = OrderItem.objects.get(pk=pk)
      serializer = OrderItemSerializer(order_item)
      return Response(serializer.data)
    except OrderItem.DoesNotExist as ex:
      return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

  def list(self, request):
    """Handles GET request for all order items"""
    
    order_item = OrderItem.objects.all()
    serializer = OrderItemSerializer(order_item, many=True)
    return Response(serializer.data)
  
  def destroy(self, request, pk):
    """Handles DELETE request for order item"""
    item = OrderItem.objects.get(pk=pk)
    item.delete()
    return Response(None, status=status.HTTP_204_NO_CONTENT)
  
  def create(self, request):
    """Handles POST request for adding items to order"""
    
    order = Order.objects.get(pk=request.data["order"])
    item = Item.objects.get(pk=request.data["item"])
    
    order_item = OrderItem.objects.create(
      order=order,
      item=item,
    )
    serializer = OrderItemSerializer(order_item)
    return Response(serializer.data)
  
class OrderItemSerializer(serializers.ModelSerializer):
  class Meta:
    model = OrderItem
    fields = ('id', 'order', 'item')
