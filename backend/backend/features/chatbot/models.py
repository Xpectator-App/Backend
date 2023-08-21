from django.db import models
import uuid

class Chatbot(models.Model):
    class Meta:
        db_table = 'chatbot'
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __unicode__(self):
        return self.name
    
    def __str__(self):
        return self.name


class Message(models.Model):
    class Meta:
        db_table = 'message'
        
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.UUIDField()
    chatbot_id = models.UUIDField()
    message_from = models.CharField(max_length=20)
    message_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __unicode__(self):
        return self.name
    
    def __str__(self):
        return self.name
