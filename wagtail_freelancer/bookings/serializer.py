from rest_framework import serializers

from bookings.models import Meeting

#serializer = turning model data -> JSON
class MeetingSerializer(serializers.ModelSerializer):
	class Meta:
		model = Meeting
		fields = ('id', 'name', 'email', 'phone_number', 'day_time')