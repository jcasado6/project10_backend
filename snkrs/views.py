from rest_framework import generics, permissions
from .serializers import UserSerializer, WishlistSerializer, OwnedSerializer
from .models import User, Owned, Wishlist

# Create your views here.

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)

class WishlistList(generics.ListCreateAPIView):
    queryset = Wishlist.objects.all()
    serializer_class = WishlistSerializer
    permission_classes = (permissions.IsAuthenticated,)

class WishlistDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Wishlist.objects.all()
    serializer_class = WishlistSerializer
    permission_classes = (permissions.IsAuthenticated,)

class OwnedList(generics.ListCreateAPIView):
    queryset = Owned.objects.all()
    serializer_class = OwnedSerializer
    permission_classes = (permissions.IsAuthenticated,)

class OwnedDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Owned.objects.all()
    serializer_class = OwnedSerializer
    permission_classes = (permissions.IsAuthenticated,)



