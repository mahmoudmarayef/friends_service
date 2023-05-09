from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer, FriendshipSerializer
from .models import Friendship
from django.db.models import Q


class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FriendshipCreateView(generics.CreateAPIView):
    serializer_class = FriendshipSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class IncomingFriendRequestsView(generics.ListAPIView):
    serializer_class = FriendshipSerializer

    def get_queryset(self):
        user = self.request.user
        # Get the incoming friend requests for the user
        return Friendship.objects.filter(to_user=user, status='pending')


class OutgoingFriendRequestsView(generics.ListAPIView):
    serializer_class = FriendshipSerializer

    def get_queryset(self):
        user = self.request.user
        # Get the outgoing friend requests from the user
        return Friendship.objects.filter(from_user=user, status='pending')


class FriendshipUpdateView(generics.UpdateAPIView):
    serializer_class = FriendshipSerializer

    def get_queryset(self):
        user = self.request.user
        return Friendship.objects.filter(
            to_user=user,
            from_user=self.kwargs['pk'],
            status='pending'
        )

    def put(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if queryset.exists():
            friendship = queryset.first()
            friendship.status = request.data.get('status', friendship.status)
            friendship.save()
            serializer = self.get_serializer(friendship)
            return Response(serializer.data)
        else:
            return Response({'error': 'Friendship object does not exist.'}, status=404)


class FriendshipDeleteView(generics.DestroyAPIView):
    serializer_class = FriendshipSerializer

    def get_queryset(self):
        user = self.request.user
        # Get the friendship object between the user and the other user
        return Friendship.objects.filter(
            (Q(from_user=user, to_user=self.kwargs['pk']) |
             Q(from_user=self.kwargs['pk'], to_user=user)),
            status='confirmed'
        )

    def delete(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if queryset.exists():
            friendship = queryset.first()
            friendship.delete()
            return Response({'success': 'Friendship deleted.'})
        else:
            return Response({'error': 'Friendship object does not exist.'}, status=404)