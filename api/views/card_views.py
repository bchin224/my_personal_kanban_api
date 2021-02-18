from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, status
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user, authenticate, login, logout
from django.middleware.csrf import get_token

from ..models.card import Card
from ..serializers import CardSerializer, UserSerializer

# Create your views here.
class Cards(generics.ListCreateAPIView):
    permission_classes=(IsAuthenticated,)
    serializer_class = CardSerializer
    def get(self, request):
        """Index request"""
        # Get all the cardss:
        # cards = Card.objects.all()
        # Filter the cards by owner, so you can only see your owned kanban cards
        cards = Card.objects.filter(owner=request.user.id)
        # Run the data through the serializer
        data = CardSerializer(cards, many=True).data
        return Response({ 'cards': data })

    def post(self, request):
        """Create request"""
        # Add user to request data object
        request.data['card']['owner'] = request.user.id
        # Serialize/create card
        card = CardSerializer(data=request.data['card'])
        # If the card data is valid according to our serializer...
        if card.is_valid():
            # Save the created card & send a response
            card.save()
            return Response({ 'card': card.data }, status=status.HTTP_201_CREATED)
        # If the data is not valid, return a response with the errors
        return Response(card.errors, status=status.HTTP_400_BAD_REQUEST)

class CardDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=(IsAuthenticated,)
    def get(self, request, pk):
        """Show request"""
        # Locate the card to show
        card = get_object_or_404(Card, pk=pk)
        # Only want to show owned cards?
        if not request.user.id == card.owner.id:
            raise PermissionDenied('Unauthorized, this is not on your kanban board')

        # Run the data through the serializer so it's formatted
        data = CardSerializer(card).data
        return Response({ 'card': data })

    def delete(self, request, pk):
        """Delete request"""
        # Locate kanban card to delete
        card = get_object_or_404(Card, pk=pk)
        # Check the card's owner against the user making this request
        if not request.user.id == card.owner.id:
            raise PermissionDenied('Unauthorized, this is not on your kanban board.')
        # Only delete if the user owns this kanban card
        card.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def partial_update(self, request, pk):
        """Update Request"""
        # Remove owner from request object
        # This "gets" the owner key on the data['card'] dictionary
        # and returns False if it doesn't find it. So, if it's found we
        # remove it.
        if request.data['card'].get('owner', False):
            del request.data['card']['owner']

        # Locate Card
        # get_object_or_404 returns a object representation of our Card
        card = get_object_or_404(Card, pk=pk)
        # Check if user is the same as the request.user.id
        if not request.user.id == card.owner.id:
            raise PermissionDenied('Unauthorized, this is not on your kanban board.')

        # Add owner to data object now that we know this user owns the resource
        request.data['card']['owner'] = request.user.id
        # Validate updates with serializer
        data = CardSerializer(card, data=request.data['card'])
        if data.is_valid():
            # Save & send a 204 no content
            data.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        # If the data is not valid, return a response with the errors
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)
