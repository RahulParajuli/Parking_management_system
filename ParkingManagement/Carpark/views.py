from datetime import datetime
from .models import Parkbay, BayBooking
from rest_framework.views import APIView
from ParkingManagement.utils import saturate_date
from Carpark.ResponseHelper.response import ResponseHelper
from .serializers import BookingSerializer, ParkbaySerializer

class Parkbaylist(APIView):
    def get(self, request):
        """
        This method is used to fetch all the parkbays
        request type: GET
        input: None
        output: bay_number, Booked, date
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
        request type: GET
        input: None
        output: name, license_plate, booking_date, booking_for, booking_status, bay_number
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
        request type: POST
        input: name, license_plate, booking_date, booking_for
        output: booking_status, bay_number
        """
        book_data = request.data
        booking_date = saturate_date(book_data['booking_for'])

        try:
            if booking_date[0] == "":
                return ResponseHelper.get_bad_request_response("Please provide booking date") 

            booking_details = BayBooking.objects.filter(booking_for = booking_date[0])
            liscence_plate = booking_details.values('license_plate')
            if liscence_plate :
                for _ in liscence_plate:
                    if _['license_plate'] == book_data['license_plate']:
                        return ResponseHelper.get_conflict_response("Liscence plate already registered")

            if booking_date[1] <= datetime.now():
                return ResponseHelper.get_conflict_response("Cannot book for past days")

            try:
                booked_bays =  BayBooking.objects.filter(booking_for = booking_date[0])
                booked_data = booked_bays.values().count()

                if booked_data < 4:
                    Bay = Parkbay.objects.create(bay_number=booked_data+1,
                                                 booked=True,
                                                 date = booking_date[1])
                    
                    Bookpark = BayBooking.objects.create(booking_status=True,
                                                            booked_bay_number=int(Bay.bay_number), 
                                                            name=book_data['name'],
                                                            license_plate=book_data['license_plate'],
                                                            booking_date=datetime.now(),
                                                            booking_for=booking_date[1]
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

                    return ResponseHelper.get_success_response(result,"Booking Placed successfully")
                else:
                    return ResponseHelper.get_conflict_response("No parking bays available")
            except Exception as err:
                print(err)
                return ResponseHelper.get_bad_request_response("Bad request")
        except Exception as e:
            print(e)
            return ResponseHelper.get_bad_request_response("Bad request")
    
#get all available bays
class AllAvailableBaylist(APIView):
    def get(self, request):
        """
        This method is used to fetch all available parking bays for a date
        request type: GET
        input: None
        output: bay_number
        """
        try:
            if Parkbay.objects.filter(booked=False).exists():
                Bay = Parkbay.objects.filter(booked=False)
                serializer = ParkbaySerializer(Bay, many=True)
                return ResponseHelper.get_success_response(serializer.data, "Successfully fetched available bays")
            return ResponseHelper.get_bad_request_response("No parking bays available")
        except Exception as e:
            print(e)
            return ResponseHelper.get_bad_request_response("Bad request")

class AllBookedBaylist(APIView):
    def get(self, request):
        """
        This method is used to fetch all booked parking bays for a date
        request type: GET
        input: None
        output: bay_number
        """
        try:
            if Parkbay.objects.filter(booked=True).exists():
                Bay = Parkbay.objects.filter(booked=True)
                serializer = ParkbaySerializer(Bay, many=True)
                return ResponseHelper.get_success_response(serializer.data, "Successfully fetched booked bays")
            return ResponseHelper.get_bad_request_response("No parking bays booked")
        except Exception as e:
            print(e)
            return ResponseHelper.get_bad_request_response("Bad request")

class BookedBayDates(APIView):
    def get(self, request, date):
        """
        This method is used to fetch all booked parking bays for a date
        request type: GET
        input: date
        output: bay_number
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
        except Exception as e:
            print(e)
            return ResponseHelper.get_bad_request_response("Bad request")

#list all the booking made in a date
class BookedBayList(APIView):
    def post(self, request):
        """
        This method is used to fetch all booked parking bays for a date
        request type: POST
        input: None
        output: booking_status, bay_number
        """
        query_data = request.data['date']
        query_date = saturate_date(query_data)
        try:
            if query_data == "":
                return ResponseHelper.get_bad_request_response("Please provide booking date")
            else:
                if BayBooking.objects.filter(booking_for=query_date[1]).exists():
                    booked = BayBooking.objects.filter(booking_for=query_date[1])
                    booked_data = BookingSerializer(booked, many=True)
                    result = {
                        "name": booked_data.data[0]['name'],
                        "license_plate": booked_data.data[0]['license_plate'],
                        "booking_date": booked_data.data[0]['booking_date'],
                        "booking_for": query_data,
                        "booking_status": booked_data.data[0]['booking_status'],
                        "booked_bay_number": booked_data.data[0]['booked_bay_number']

                    }
                    return ResponseHelper.get_success_response(result, "Successfully fetched booked data")
                return ResponseHelper.get_bad_request_response("No parking bays booked")
        except Exception as e:
            print(e)
            return ResponseHelper.get_bad_request_response("Bad request")