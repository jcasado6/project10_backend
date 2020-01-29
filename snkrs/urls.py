from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('users/', views.UserList.as_view(), name='user_list'),

    path('users/<int:pk>', views.UserDetail.as_view(), name='user_detail'),

    path('owned/', views.OwnedList.as_view(), name="owned_list"),

    path('owned/<int:pk>', views.OwnedDetail.as_view(), 
    name="owned_detail"),

    path('wishlist/', views.WishlistList.as_view(), name="wishlist_list"),

    path('wishlist/<int:pk>', views.WishlistDetail.as_view(), name="wishlist_detail"),
]