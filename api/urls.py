from rest_framework import routers
from api.views import FriendViewSet, BelongingViewSet, BorrowedViewSet
from django.urls import path

# Initialize the DefaultRouter class from routers
router = routers.DefaultRouter()

# Register each views into the router
router.register(r'belongings', BelongingViewSet)
router.register(r'borrowings', BorrowedViewSet)
router.register(r'friends', FriendViewSet)
