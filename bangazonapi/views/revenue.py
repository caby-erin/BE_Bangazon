from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from bangazonapi.models import Revenue

class RevenueView(ViewSet):
  def retrieve(self, request, pk):
    revenue = Revenue.objects.get(pk=pk)
    serializer = RevenueSerializer(revenue)
    return Response(serializer.data)
  
  def list(self, request):
    revenues = Revenue.objects.all()
    serializer = RevenueSerializer(revenues, many=True)
    return Response(serializer.data)

class RevenueSerializer(serializers.ModelSerializer):
  class Meta:
    model = Revenue
    fields = ('id', 'order', 'total_order_amount', 'tip_amount')
