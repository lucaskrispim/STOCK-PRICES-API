from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import StockCandleSerializerPandas
import yfinance as yf

# Create your views here.
class CandlestickByStock(APIView):
    def get(self, request, format=None):
        try:
            data = yf.download(request.query_params['stock']+".SA",start=request.query_params['start'], end=request.query_params['end'])
            data.rename(columns={'Adj Close': 'Adj_Close'}, inplace=True)
            data['data'] = data.index

        except Exception as e:
            return Response(
            {
                "message": "Erro na obtenção de dados da empresa",
            },
            status=status.HTTP_400_BAD_REQUEST)
        
        companyCandleSerialized = StockCandleSerializerPandas(data.to_dict('records'), many=True)
        
        return Response(companyCandleSerialized.data,status=status.HTTP_200_OK)
