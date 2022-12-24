from .models import BayBooking, Parkbay
from rest_framework import serializers

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = BayBooking
        fields = ('name', 'license_plate', 'booking_date', 'booking_for', 'booking_status', "booked_bay_number")

class ParkbaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Parkbay
        fields = ('bay_number', 'booked', 'date')