from django.test import TestCase
from restaurant.views import BookingViewSet
from restaurant.serializers import BookingSerializer
from restaurant.models import Booking
from datetime import datetime

class BookingTest(TestCase):
    def setUp(self):
        Booking.objects.create(name="Dany", no_of_guests=2, booking_date=datetime.now())
        Booking.objects.create(name="Tony", no_of_guests=3, booking_date=datetime.now())
    
    def test_get_all(self):
        items = BookingSerializer(Booking.objects.all(), many=True)
        self.assertEqual(len(items.data), 2)

        self.assertEqual(items.data[0]['name'], "Dany")
        self.assertEqual(items.data[0]['no_of_guests'], 2)

        self.assertEqual(items.data[1]['name'], "Tony")
        self.assertEqual(items.data[1]['no_of_guests'], 3)