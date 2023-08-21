from django.urls import path
from . import views

urlpatterns = [
    path('chatbot/', views.ChatbotListCreateView.as_view()),
    path('chatbot/<int:pk>/', views.ChatbotRetrieveUpdateDestroyView.as_view()),
    path('message/', views.MessageListCreateView.as_view()),
    path('message/<int:pk>/', views.MessageRetrieveUpdateDestroyView.as_view()),
]