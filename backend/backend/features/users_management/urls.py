from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('check-user/', views.CheckUserByEmail.as_view(), name='check-user'),
    path('profile/', views.ProfileListCreateView.as_view(), name='profile-list-create'),
    path('profile/<uuid:pk>/', views.ProfileRetrieveUpdateDestroyView.as_view(), name='profile-retrieve-update-destroy'),
    path('user/', views.UserListCreateView.as_view(), name='user-list-create'),
    path('user/<uuid:pk>/', views.UserRetrieveUpdateDestroyView.as_view(), name='user-retrieve-update-destroy'),
]
