from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User,Group
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model=Group
        fields="__all__"
class UserSerializer(serializers.ModelSerializer):
    groups = GroupSerializer(many=True, read_only=True)  
    class Meta:
        model = User
        fields = ['id','username', 'email', 'is_active', 'password', 'groups']
        extra_kwargs = {
            'password': {'write_only': True},
            'id': {'read_only': True},
            
        }

    def create(self, validated_data):
        group_name = validated_data.pop('groups', None)
        user = User(**validated_data)
        user.set_password(validated_data['password'])  
        user.save()
        if group_name:
            try:
                group = Group.objects.get(name=group_name)
                user.groups.add(group)
            except Group.DoesNotExist:
                raise serializers.ValidationError(f"Le groupe '{group_name}' n'existe pas.")
 
        return user
class ProduitEnCommandeSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProduitEnCommande
        fields="__all__"


class CommandeSerializer(serializers.ModelSerializer):
    produits=ProduitEnCommandeSerializer(source='produits_en_commandes',many=True)
    class Meta:
        model=Commande
        fields=['etat_CHOICES', 'client', 'dateCommande', 'note', 'etatCommande','produits']
class RemisesSerializer(serializers.ModelSerializer):
    client=UserSerializer(many=True)
    class Meta:
        model=Remises
        fields="__all__"
class FeedBackSerializer(serializers.ModelSerializer):
    client=UserSerializer(many=True)
    class Meta:
        model=FeedBack
        fields="__all__"

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
            token = super().get_token(user)
            user_data = UserSerializer(user).data
            token['user'] = user_data
            print(token)
            return token
    def validate(self, attrs):
        data = super().validate(attrs)
        user_data = UserSerializer(self.user).data
        data['user'] = user_data  # Ajoutez les données utilisateur à la réponse
        return data