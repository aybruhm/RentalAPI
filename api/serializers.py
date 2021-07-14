from rest_framework import serializers
from api.models import Friend, Belonging, Borrowed



class FriendSerializer(serializers.ModelSerializer):

	class Meta:
		model = Friend
		fields = "__all__"


class BelongingSerializer(serializers.ModelSerializer):

	class Meta:
		model = Belonging
		fields = "__all__"


class BorrowedSerializer(serializers.ModelSerializer):

	class Meta:
		model = Borrowed
		fields = "__all__"