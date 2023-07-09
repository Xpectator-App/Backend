from rest_framework import serializers
from .models import Event, EventTeam, EventsPhoto, EventsReview, Location, Sport, Team

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

class EventTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventTeam
        fields = '__all__'

class EventsPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventsPhoto
        fields = '__all__'

class EventsReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventsReview
        fields = '__all__'

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'

class SportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sport
        fields = '__all__'

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'
