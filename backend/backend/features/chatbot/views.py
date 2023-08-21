from rest_framework import generics
from .models import Chatbot, Message
from .serializers import ChatbotSerializer, MessageSerializer

class ChatbotListCreateView(generics.ListCreateAPIView):
    queryset = Chatbot.objects.all()
    serializer_class = ChatbotSerializer
    

class ChatbotRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Chatbot.objects.all()
    serializer_class = ChatbotSerializer
    

class MessageListCreateView(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    

class MessageRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer