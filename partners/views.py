from .models import * 
from .serializers import * 
from django.contrib.auth.models import User,Group
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny,IsAdminUser
from rest_framework import response,status
from rest_framework_simplejwt.authentication import JWTAuthentication
class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    authentication_classes=[JWTAuthentication] 
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticated]

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    authentication_classes=[JWTAuthentication] 
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
class CommandeViewSet(viewsets.ModelViewSet):
    queryset = Commande.objects.all()
    authentication_classes=[JWTAuthentication] 
    serializer_class = CommandeSerializer
    permission_classes = [IsAuthenticated]
class ProduitEnCommandeViewSet(viewsets.ModelViewSet):
    queryset = ProduitEnCommande.objects.all()
    authentication_classes=[JWTAuthentication] 
    serializer_class = ProduitEnCommandeSerializer
    permission_classes = [IsAuthenticated]
