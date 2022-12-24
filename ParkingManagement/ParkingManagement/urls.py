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

urlpatterns = [
    path('admin/', admin.site.urls), #access admin panel - ID = rahul, password = rahul
    path('booking', views.Bookinglist.as_view()), #get booking list and make booking
    path('parkbay', views.Parkbaylist.as_view()), #get parkbay list
    path('bookedbays', views.AllBookedBaylist.as_view()), #get all booked bays
    path('availablebaylist', views.AllAvailableBaylist.as_view()), #get all available bays
    path('date/bookinglist', views.BookedBayList.as_view()), #get all booked bays for a date
    path("bookinglist/<str:date>/", views.BookedBayDates.as_view()), #get all booked bays for a date
]
