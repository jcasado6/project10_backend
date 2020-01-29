from rest_framework import serializers
from .models import Owned, Wishlist, User

class OwnedSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Owned
        fields = ('name', 'brand', 'model', 'retail_price', 'release_date', 'img')

class WishlistSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Wishlist
        fields = ('name', 'brand', 'model', 'retail_price', 'release_date', 'img')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    owns = serializers.HyperlinkedRelatedField(view_name='owned_detail',
    read_only=True
    )
    
    wishlist = serializers.HyperlinkedRelatedField(
        view_name='wishlist_detail',
        read_only=True
    )

    class Meta:
        model = User
        fields = ('name', 'owns', 'wishlist', 'img')


    