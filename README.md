## Parking Reservation API

This API allows users to access a park bay booking functionality as per the pre-determined terms and conditions mentioned in the assigned task.


### Getting Started


To get started with the API, you will need to set up a Python development environment and install the necessary dependencies.

* Install Python **3.10** or later
* Clone the repository:
<code> git clone https://github.com/RahulParajuli/Parking_management_system.git<code>
* Install the required packages using the command: <code> pip install -r requirements.txt </code>
* Navigate to the project directory.
* To run the app try command <code>python manage.py runserver</code>
* To run unit test apply the command <code>./manage.py test</code>
* The **postman collection** for each API can be found in the root folder as *postman_collection.json*.

<hr>
### Endpoints
The API has multiple endpoints available for accessing the mentioned features and functionalities in the assignment. You can find a full list of endpoints and their descriptions in the API documentation accesbile through the endpoint <code>/redocs</code>.

<hr>
#### Assumptions Made During The Development

<b>Function I : Booking of A Parking Bay</b>

1. A customer can only book a singular park bay designated to a vehicle for a particular day. 
**More than one reservations for the same vehicle cannot be made.** Vehicles are identified with the use of license plate numbers which is considered to be a universally unique constraint. However, booking for two different vehicles by the same customer or two different ones with a common name is possible in case the booking is being placed for a new vehicle.

*Note: User who have booked are also stored in parkbay database to query  which user has booked a particular bay*

2. The booking endpoint <code>/booking</code> handles the reservation of the request for the following date formats. 
i. 1st Jan 2023 (The date sample presented in the test case)
ii. 2023-01-01 (A standard date format) 

Meanwhile the date in the database is stored in as %Y-%M-%D datetime object. 

3. The date field cannot be sent empty during a booking. 

4. All the reservations are to made a day ahead. Any requests made for the day or the day past will not be allowed.

5. Due to the limitation in park bays, only 4 bookings can be made for a particular date.

6. There are situational **edge case** where user can make booking for any future dates, to understand and overcome this situation the booking has been limited to a month for future dates.

<b>Function II : Get The Reservations</b>

1. Similar to the booking, the quering of the reservations is handled in the following date formats.

i. 1st Jan 2023 (The date sample presented in the test case)
ii. 2023-01-01 (A standard date format)
iii. The booking detail can be queried for a given date using two approaches
* Posting date in /date/bookinglist route
* By passing date in url /bookinglist/< date>
<hr>


 *Note- The <code>db.sqlite3</code> file contains dummy data for the system which has been added with the consideration of providing initial aid for testing.*