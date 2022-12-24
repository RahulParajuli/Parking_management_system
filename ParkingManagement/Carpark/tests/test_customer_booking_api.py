import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from Carpark.models import Parkbay, BayBooking
from Carpark.views import Parkbaylist, Bookinglist
from Carpark.serializers import BookingSerializer, ParkbaySerializer

# initialize the APIClient app
client = Client()

#get booking list
class GetAllBookingsTest(TestCase):
    """Test module for getting all the bookings"""
    
    def setUp(self):
        Parkbay.objects.create(bay_number=1, booked=False, date="2020-09-10")
        Parkbay.objects.create(bay_number=2, booked=False, date="2020-09-10")
        BayBooking.objects.create(name="test user 1", license_plate="DL 1A 1234", booking_for="2020-09-10", booked_bay_number=1, booking_status=False, booking_date="2022-12-26")
        BayBooking.objects.create(name="test user 2", license_plate="DL 1A 12345", booking_for="2020-09-10", booked_bay_number=2, booking_status=False, booking_date="2022-12-26")
        # BayBooking.objects.create(name="test user 2", license_plate="DL 1A 12345", booking_for="2020-09-10", booked_bay_number=2, booking_status=False, booking_date="1st Jan 2023")
        BayBooking.objects.create(name="test user 2", license_plate="DL 1A 12345", booking_for="2020-09-10", booked_bay_number=2, booking_status=False, booking_date="2022-12-27")

    def test_get_all_bookings(self):
        response = client.get(reverse("booking"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

# post a booking
class PostBookingTest(TestCase):
    """Test module for posting a booking"""
    
    def setUp(self):
        Parkbay.objects.create(bay_number=1, booked=False, date="2020-09-10")
        Parkbay.objects.create(bay_number=2, booked=False, date="2020-09-10")
        BayBooking.objects.create(name="test user 1", license_plate="DL 1A 1234", booking_for="2020-09-10", booked_bay_number=1, booking_status=False, booking_date="2022-12-26")
        BayBooking.objects.create(name="test user 2", license_plate="DL 1A 12345", booking_for="2020-09-10", booked_bay_number=2, booking_status=False, booking_date="2022-12-26")
        # BayBooking.objects.create(name="test user 2", license_plate="DL 1A 12345", booking_for="2020-09-10", booked_bay_number=2, booking_status=False, booking_date="1st Jan 2023")

    def test_post_booking(self):
        valid_payload = {
            "name": "test user 3",
            "license_plate": "DL 1A 123456",
            "booking_for": "2023-01-10"
        }
        response = client.post(
            reverse("booking"),
            data=json.dumps(valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

# get booking by booking_for date
class GetBookingByDateTest(TestCase):
    """Test module for getting a booking by booking_for date"""
    
    def setUp(self):
        Parkbay.objects.create(bay_number=1, booked=False, date="2022-12-30")
        Parkbay.objects.create(bay_number=2, booked=False, date="2020-12-30")
        BayBooking.objects.create(name="test user 1", license_plate="DL 1A 1234", booking_for="2022-12-30", booked_bay_number=1, booking_status=False, booking_date="2022-12-31")
        BayBooking.objects.create(name="test user 2", license_plate="DL 1A 12345", booking_for="2022-12-31", booked_bay_number=2, booking_status=False, booking_date="2023-01-10")
        # BayBooking.objects.create(name="test user 2", license_plate="DL 1A 12345", booking_for="2020-09-10", booked_bay_number=2, booking_status=False, booking_date="1st Jan 2023")

    def test_get_booking_by_date(self):
        response = client.get(reverse("bookinglistDate", kwargs={'date': "2022-12-31"}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class GetBookingByDatePostTest(TestCase):
    """Test module for getting a booking by booking_for date"""
    
    def setUp(self):
        Parkbay.objects.create(bay_number=1, booked=False, date="2022-12-30")
        Parkbay.objects.create(bay_number=2, booked=False, date="2020-12-30")
        BayBooking.objects.create(name="test user 1", license_plate="DL 1A 1234", booking_for="2022-12-30", booked_bay_number=1, booking_status=False, booking_date="2022-12-31")
        BayBooking.objects.create(name="test user 2", license_plate="DL 1A 12345", booking_for="2022-12-31", booked_bay_number=2, booking_status=False, booking_date="2023-01-10")
        # BayBooking.objects.create(name="test user 2", license_plate="DL 1A 12345", booking_for="2020-09-10", booked_bay_number=2, booking_status=False, booking_date="1st Jan 2023")

    def test_get_booking_by_date(self):
        valid_payload = {
            "date": "2022-12-31",
        }
        response = client.post(
            reverse("dateBookinglist"),
            data=json.dumps(valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)



