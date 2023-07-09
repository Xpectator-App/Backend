from rest_framework import generics
from .models import Event, EventTeam, EventsPhoto, EventsReview, Location, Sport, Team
from .serializers import EventSerializer, EventTeamSerializer, EventsPhotoSerializer, EventsReviewSerializer, LocationSerializer, SportSerializer, TeamSerializer

class EventListCreateView(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    

class EventRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    

class EventTeamListCreateView(generics.ListCreateAPIView):
    queryset = EventTeam.objects.all()
    serializer_class = EventTeamSerializer
    

class EventTeamRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = EventTeam.objects.all()
    serializer_class = EventTeamSerializer
    

class EventsPhotoListCreateView(generics.ListCreateAPIView):
    queryset = EventsPhoto.objects.all()
    serializer_class = EventsPhotoSerializer
    

class EventsPhotoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = EventsPhoto.objects.all()
    serializer_class = EventsPhotoSerializer
    

class EventsReviewListCreateView(generics.ListCreateAPIView):
    queryset = EventsReview.objects.all()
    serializer_class = EventsReviewSerializer
    

class EventsReviewRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = EventsReview.objects.all()
    serializer_class = EventsReviewSerializer
    

class LocationListCreateView(generics.ListCreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    

class LocationRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    

class SportListCreateView(generics.ListCreateAPIView):
    queryset = Sport.objects.all()
    serializer_class = SportSerializer
    

class SportRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sport.objects.all()
    serializer_class = SportSerializer

class TeamListCreateView(generics.ListCreateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    

class TeamRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

