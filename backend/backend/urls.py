from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v0/', include([
        path('', include('backend.features.users_management.urls')),
        path('', include('backend.features.sport_events.urls')),
        path('', include('backend.features.chatbot.urls')),
    ])),
]