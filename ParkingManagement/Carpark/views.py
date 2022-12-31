from datetime import datetime, timedelta
from .models import Parkbay, BayBooking
from rest_framework.views import APIView
from ParkingManagement.utils import saturate_date
from Carpark.ResponseHelper.response import ResponseHelper
from .serializers import BookingSerializer, ParkbaySerializer

class Parkbaylist(APIView):
    def get(self, request):
        """
        This method is used to fetch all the parkbays
        Request type: GET
        Args: None
        Return: bay_number, Booked, date
        """
        try:
            ParkbayList = Parkbay.objects.all()
            serializer = ParkbaySerializer(ParkbayList, many=True)
            return ResponseHelper.get_success_response(serializer.data, "Successfully fetched parkbay")
        except:
            return ResponseHelper.get_bad_request_response("No data found")

class Bookinglist(APIView):
    def get(self, request):
        """
        This method is used to fetch all the bookings
        Request type: GET
        Args: None
        Return: name, license_plate, booking_date, booking_for, booking_status, bay_number
        """
        try:
            BookingList = BayBooking.objects.all()
            serializer = BookingSerializer(BookingList, many=True)
            return ResponseHelper.get_success_response(serializer.data, "Successfully fetched booking")
        except:
            return ResponseHelper.get_bad_request_response("No data found")

    def post(self, request):
        """
        This method is used to book a parking bay
        Request type: POST
        Args: name, license_plate, booking_date, booking_for
        Return: booking_status, bay_number
        """
        book_data = request.data
        booked_for = saturate_date(book_data['booking_for'])

        try:
            if book_data['booking_for'] == "" or book_data['name'] == "" or book_data['license_plate'] == "":
                return ResponseHelper.get_bad_request_response("Please provide booking date, name and liscence plate") 

            booking_details = BayBooking.objects.filter(booking_for = booked_for[0])
            liscence_plate = booking_details.values('license_plate')

            if liscence_plate:
                for _ in liscence_plate:
                    if _['license_plate'] == book_data['license_plate']:
                        return ResponseHelper.get_conflict_response("Liscence plate already registered")

            week = datetime.now() + timedelta(days=30)
            week_date = datetime.strftime(week, "%Y-%m-%d")
            booked_date = datetime.strftime(booked_for[1], "%Y-%m-%d")

            if booked_date > week_date:
                return ResponseHelper.get_conflict_response("Cant book the bay for more than 30 days")

            if booked_for[1] <= datetime.now():
                return ResponseHelper.get_conflict_response("Cannot book for previous dates, please select a future date")

            try:
                booked_bays =  BayBooking.objects.filter(booking_for = booked_for[0])
                booked_data = booked_bays.values().count()

                if booked_data < 4:
                    Bay = Parkbay.objects.create(bay_number=booked_data+1,
                                                 booked=True,
                                                 date = booked_for[1],
                                                 customer=book_data['name'])
                    
                    Bookpark = BayBooking.objects.create(booking_status=True,
                                                            booked_bay_number=int(Bay.bay_number), 
                                                            name=book_data['name'],
                                                            license_plate=book_data['license_plate'],
                                                            booking_date=datetime.now(),
                                                            booking_for=booked_for[1]
                                                            )
                    
                    Bookpark.save()
                    
                    result = {
                        "name": Bookpark.name,
                        "license_plate": Bookpark.license_plate,
                        "booking_date": Bookpark.booking_date,
                        "booking_for": book_data['booking_for'],
                        "booking_status": Bookpark.booking_status,
                        "booked_bay_number": Bookpark.booked_bay_number
                    }

                    return ResponseHelper.get_created_response(result,"Booking Placed successfully")
                else:
                    return ResponseHelper.get_conflict_response("No parking bays available for the day")
            except Exception as err:
                print(err)
                return ResponseHelper.get_bad_request_response("Bad request")
        except Exception as err:
            print(err)
            return ResponseHelper.get_bad_request_response("Bad request")
    
#get all available bays
class AllAvailableBaylist(APIView):
    def get(self, request):
        """
        This method is used to fetch all available parking bays for a date
        Request type: GET
        Args: None
        Return: bay_number
        """
        try:
            if Parkbay.objects.filter(booked=False).exists():
                Bay = Parkbay.objects.filter(booked=False)
                serializer = ParkbaySerializer(Bay, many=True)
                return ResponseHelper.get_success_response(serializer.data, "Successfully fetched available bays")
            return ResponseHelper.get_bad_request_response("No parking bays available")
        except:
            return ResponseHelper.get_bad_request_response("Bad request")

class AllBookedBaylist(APIView):
    def get(self, request):
        """
        This method is used to fetch all booked parking bays for a date
        Request type: GET
        Args: None
        Return: bay_number
        """
        try:
            if Parkbay.objects.filter(booked=True).exists():
                Bay = Parkbay.objects.filter(booked=True)
                serializer = ParkbaySerializer(Bay, many=True)
                return ResponseHelper.get_success_response(serializer.data, "Successfully fetched booked bays")
            return ResponseHelper.get_bad_request_response("No parking bays booked")
        except:
            return ResponseHelper.get_bad_request_response("Bad request")

class BookedBayDates(APIView):
    def get(self, request, date):
        """
        This method is used to fetch all booked parking bays for a date
        Request type: GET
        Args: date
        Return: bay_number
        """
        try:
            if BayBooking.objects.filter(booking_for=date.strip()).exists():
                booked = BayBooking.objects.filter(booking_for=date.strip())
                booked_data = BookingSerializer(booked, many=True)
                result = {
                    "booked_data": booked_data.data
                }
                return ResponseHelper.get_success_response(result, "Successfully fetched booked data")
            return ResponseHelper.get_bad_request_response("No parking bays booked")
        except:
            return ResponseHelper.get_bad_request_response("Bad request")

#list all the booking made in a date
class BookedBayList(APIView):
    def post(self, request):
        """
        This method is used to fetch all booked parking bays for a date
        Request type: POST
        Args: None
        Return: booking_status, bay_number
        """
        query_data = request.data['date']
        query_date = saturate_date(query_data)
        try:
            if query_data == "":
                return ResponseHelper.get_bad_request_response("Please provide booking date")
            else:
                if BayBooking.objects.filter(booking_for=query_date[0]).exists():
                    booked = BayBooking.objects.filter(booking_for=query_date[0])
                    booked_data = BookingSerializer(booked, many=True)
                    result = {
                        "booked_data": booked_data.data

                    }
                    return ResponseHelper.get_success_response(result, "Successfully fetched booked data")
                return ResponseHelper.get_bad_request_response("No parking bays booked")
        except:
            return ResponseHelper.get_bad_request_response("Bad request")