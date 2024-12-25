# littlelemon
capstone project little lemon

superuser : admin
password : Admin123*


GET

http://127.0.0.1:8000/restaurant/

http://127.0.0.1:8000/restaurant/menu/

http://127.0.0.1:8000/restaurant/menu/1

http://127.0.0.1:8000/restaurant/booking/tables/
requires auth : bearer token

http://127.0.0.1:8000/auth/users/
requires auth : bearer token. Gives all users with admin token and only current user with non-admin token

http://127.0.0.1:8000/auth/users/me
requires auth : bearer token.

POST

http://127.0.0.1:8000/restaurant/menu/
required fields are title, price and inventory

http://127.0.0.1:8000/restaurant/booking/tables/
requires auth : bearer token
requires fields are name, no_of_guests and booking_date in format yyyy-mm-ddThh:mm

http://127.0.0.1:8000/auth/token/login
requires username and password. gives the auth token.

http://127.0.0.1:8000/auth/token/logout
requires auth using bearer token. deletes the auth token.

http://127.0.0.1:8000/restaurant/api-token-auth/
requires username and password. given auth token.

DELETE

http://127.0.0.1:8000/restaurant/menu/3