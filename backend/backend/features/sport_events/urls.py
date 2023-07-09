from django.urls import path
from . import views

urlpatterns = [
    path('events/', views.EventListCreateView.as_view(), name='event-list-create'),
    path('events/<uuid:pk>/', views.EventRetrieveUpdateDestroyView.as_view(), name='event-retrieve-update-destroy'),
    path('event_teams/', views.EventTeamListCreateView.as_view(), name='eventteam-list-create'),
    path('event_teams/<uuid:event_id>/<uuid:team_id>/', views.EventTeamRetrieveUpdateDestroyView.as_view(), name='eventteam-retrieve-update-destroy'),
    path('events_photos/', views.EventsPhotoListCreateView.as_view(), name='eventsphoto-list-create'),
    path('events_photos/<uuid:pk>/', views.EventsPhotoRetrieveUpdateDestroyView.as_view(), name='eventsphoto-retrieve-update-destroy'),
    path('events_reviews/', views.EventsReviewListCreateView.as_view(), name='eventsreview-list-create'),
    path('events_reviews/<uuid:pk>/', views.EventsReviewRetrieveUpdateDestroyView.as_view(), name='eventsreview-retrieve-update-destroy'),
    path('locations/', views.LocationListCreateView.as_view(), name='location-list-create'),
    path('locations/<uuid:pk>/', views.LocationRetrieveUpdateDestroyView.as_view(), name='location-retrieve-update-destroy'),
    path('sports/', views.SportListCreateView.as_view(), name='sport-list-create'),
    path('sports/<uuid:pk>/', views.SportRetrieveUpdateDestroyView.as_view(), name='sport-retrieve-update-destroy'),
    path('teams/', views.TeamListCreateView.as_view(), name='team-list-create'),
    path('teams/<uuid:pk>/', views.TeamRetrieveUpdateDestroyView.as_view(), name='team-retrieve-update-destroy'),
]
