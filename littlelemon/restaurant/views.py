from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView , RetrieveUpdateAPIView,DestroyAPIView
from .models import MenuItem,Booking
from .serializers import MenuItemSerializer , BookingSerializer ,UserSerializer
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import User 
from rest_framework.permissions import IsAuthenticated
# Create your views here.
class   MenuItemsView(ListCreateAPIView):
    queryset = MenuItem.objects.all() 
    serializer_class = MenuItemSerializer


class SingleMenuItemView(RetrieveUpdateAPIView,DestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer


class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

class UserViewSet(ModelViewSet):
   queryset = User.objects.all()
   serializer_class = UserSerializer
   permission_classes = [IsAuthenticated] 