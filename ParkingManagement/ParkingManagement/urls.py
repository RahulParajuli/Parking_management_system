"""ParkingManagement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from Carpark import views
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Parking Management API",
      default_version='v1',
      description="Parking Management API for booking bays",
      terms_of_service="",
      contact=openapi.Contact(email="rahul.parajuli27@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls), #access admin panel - ID = rahul, password = rahul
    path('booking', views.Bookinglist.as_view(), name='booking'), #get booking list and make booking
    path('bookedbays', views.AllBookedBaylist.as_view(), name='bookedbays'), #get all booked bays
    path('date/bookinglist', views.BookedBayList.as_view(), name= 'dateBookinglist'), #get all booked bays for a date
    path("bookinglist/<str:date>/", views.BookedBayDates.as_view(), name='bookinglistDate'), #get all booked bays for a date
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc')
]
