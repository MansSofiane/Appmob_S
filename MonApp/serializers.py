from rest_framework import serializers
from .models import *

class DepanneurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Depanneur
        fields = '__all__'

class ServicesDeDepannageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServicesDeDepannage
        fields = '__all__'
        ##
class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'
class VehiculesDeDepannageSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehiculesDeDepannage
        fields = '__all__'
class DemandesDeDepannageSerializer(serializers.ModelSerializer):
    class Meta:
        model = DemandesDeDepannage
        fields = '__all__'
class HistoriqueDesDepannagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoriqueDesDepannages
        fields = '__all__'
class AvisEtEvaluationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AvisEtEvaluations
        fields = '__all__'
class NotificationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notifications
        fields = '__all__'
class PaiementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paiements
        fields = '__all__'
class TarifsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarifs
        fields = '__all__'
