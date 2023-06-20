from rest_framework import serializers

class StockCandleSerializerPandas(serializers.Serializer):
  Open = serializers.FloatField()
  High = serializers.FloatField()
  Low = serializers.FloatField()
  Close = serializers.FloatField()
  Adj_Close = serializers.FloatField()
  Volume = serializers.FloatField() 
  data = serializers.DateTimeField()