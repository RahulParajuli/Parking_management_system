from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import Booking
from .serializers import BookingSerializer

class Bookinglist(APIView):
    def get(self, request):
        BookingList = Booking.objects.all()
        serializer = BookingSerializer(BookingList, many=True) #converts everying to json
        return Response(serializer.data)

    def post(self, request):
        serializer = BookingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        BookingList = Booking.objects.all()
        BookingList.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def put(self, request):
        BookingList = Booking.objects.all()
        BookingList.delete()
        serializer = BookingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
