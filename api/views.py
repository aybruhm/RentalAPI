from django.shortcuts import render
from rest_framework import viewsets
from api.models import Friend, Belonging, Borrowed
from api.serializers import FriendSerializer, BelongingSerializer, BorrowedSerializer


def home_page(request):
	return render(request, "api/home.html")


class FriendViewSet(viewsets.ModelViewSet):
	# get. update, retrieve and delete
	queryset = Friend.objects.all()
	serializer_class = FriendSerializer


class BelongingViewSet(viewsets.ModelViewSet):
	queryset = Belonging.objects.all()
	serializer_class = BelongingSerializer


class BorrowedViewSet(viewsets.ModelViewSet):
	queryset = Borrowed.objects.all()
	serializer_class = BorrowedSerializer