from rest_framework import generics, permissions, status
from .serializers import UserSerializer, WishlistSerializer, OwnedSerializer
from .models import User, Owned, Wishlist
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    

class WishlistList(generics.ListCreateAPIView):
    queryset = Wishlist.objects.all()
    serializer_class = WishlistSerializer
   

class WishlistDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Wishlist.objects.all()
    serializer_class = WishlistSerializer
    

class OwnedList(generics.ListCreateAPIView):
    queryset = Owned.objects.all()
    serializer_class = OwnedSerializer
    

class OwnedDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Owned.objects.all()
    serializer_class = OwnedSerializer
    




