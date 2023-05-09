from django.urls import path
from .views import UserRegistrationView, FriendshipCreateView, IncomingFriendRequestsView, \
    OutgoingFriendRequestsView, FriendshipUpdateView, FriendshipDeleteView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)

urlpatterns = [
    path('register/', UserRegistrationView.as_view()),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('request/', FriendshipCreateView.as_view()),
    path('incoming-requests/', IncomingFriendRequestsView.as_view(), name='incoming-requests'),
    path('outgoing-requests/', OutgoingFriendRequestsView.as_view(), name='outgoing-requests'),
    path('friendship/<int:pk>/update/', FriendshipUpdateView.as_view(), name='friendship-update'),
    path('friendship/<int:pk>/delete/', FriendshipDeleteView.as_view(), name='friendship-delete'),
]
