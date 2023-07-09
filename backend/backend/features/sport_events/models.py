from django.db import models
import uuid

class Event(models.Model):
    class Meta:
        db_table = 'event'
        
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    locations_id = models.UUIDField()
    name = models.CharField(max_length=50)
    start_datetime = models.DateField()
    end_datetime = models.DateField(null=True, blank=True)
    arena = models.CharField(max_length=50)
    max_participants = models.BigIntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class EventTeam(models.Model):
    class Meta:
        db_table = 'event_team'
        
    event_id = models.UUIDField()
    team_id = models.UUIDField()
    fan_since = models.DateField()
    active = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class EventsPhoto(models.Model):
    class Meta:
        db_table = 'events_photo'
        
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    event_id = models.UUIDField()
    source = models.CharField(max_length=150)
    active = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class EventsReview(models.Model):
    class Meta:
        db_table = 'events_review'
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.UUIDField()
    event_id = models.UUIDField()
    rating = models.IntegerField()
    comments = models.CharField(max_length=150, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Location(models.Model):
    class Meta:
        db_table = 'location'
        
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, null=True, blank=True)
    address = models.CharField(max_length=50)
    latitude = models.BigIntegerField(null=True, blank=True)
    longitude = models.BigIntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Sport(models.Model):
    class Meta:
        db_table = 'sport'
        
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Team(models.Model):
    class Meta:
        db_table = 'team'
        
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sport_id = models.UUIDField()
    locations_id = models.UUIDField()
    name = models.CharField(max_length=50)
    country = models.CharField(max_length=150)
    city = models.CharField(max_length=50, null=True, blank=True)
    home_arena = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

