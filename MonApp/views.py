from rest_framework import generics
from .models import Users, Depanneur, ServicesDeDepannage, VehiculesDeDepannage, DemandesDeDepannage, Notifications, Tarifs
from .serializers import UsersSerializer, DepanneurSerializer, ServicesDeDepannageSerializer, VehiculesDeDepannageSerializer, DemandesDeDepannageSerializer, NotificationsSerializer, TarifsSerializer

import logging
import pytz
import datetime
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import smart_str
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.views import APIView
# User

class UsersList(APIView):
    def get(self, request):
        User = Users.objects.all()
        serializer = UsersSerializer(User, many=True)
        return Response(serializer.data,  status=status.HTTP_201_CREATED)
    def post(self, request):
        serializer = UsersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREAT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UsersDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
    
    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)


# Depanneur
class DepanneurList(generics.ListCreateAPIView):
    queryset = Depanneur.objects.all()
    serializer_class = DepanneurSerializer
class DepanneurDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Depanneur.objects.all()
    serializer_class = DepanneurSerializer
    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

#Service
class ServicesDeDepannageList(generics.ListCreateAPIView):
    queryset = ServicesDeDepannage.objects.all()
    serializer_class = ServicesDeDepannageSerializer
class ServicesDeDepannageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ServicesDeDepannage.objects.all()
    serializer_class = ServicesDeDepannageSerializer
    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

#Vehicule
class VehiculesDeDepannageList(generics.ListCreateAPIView):
    queryset = VehiculesDeDepannage.objects.all()
    serializer_class = VehiculesDeDepannageSerializer
class VehiculesDeDepannageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = VehiculesDeDepannage.objects.all()
    serializer_class = VehiculesDeDepannageSerializer
    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

#Demandededepanage
class DemandesDeDepannageList(generics.ListCreateAPIView):
    queryset = DemandesDeDepannage.objects.all()
    serializer_class = DemandesDeDepannageSerializer
class DemandesDeDepannageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DemandesDeDepannage.objects.all()
    serializer_class = DemandesDeDepannageSerializer
    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

#Historiquedesdepannages
class HistoriqueDesDepannagesList(generics.ListCreateAPIView):
    queryset = DemandesDeDepannage.objects.all()
    serializer_class = DemandesDeDepannageSerializer
class HistoriqueDesDepannagesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DemandesDeDepannage.objects.all()
    serializer_class = DemandesDeDepannageSerializer
    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

#Avis
class AvisEtEvaluationsList(generics.ListCreateAPIView):
    queryset = DemandesDeDepannage.objects.all()
    serializer_class = DemandesDeDepannageSerializer
class AvisEtEvaluationsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DemandesDeDepannage.objects.all()
    serializer_class = DemandesDeDepannageSerializer
    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

#Paimenets
class PaiementsList(generics.ListCreateAPIView):
    queryset = DemandesDeDepannage.objects.all()
    serializer_class = DemandesDeDepannageSerializer
class PaiementsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DemandesDeDepannage.objects.all()
    serializer_class = DemandesDeDepannageSerializer
    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

#notification
class NotificationsList(generics.ListCreateAPIView):
    queryset = DemandesDeDepannage.objects.all()
    serializer_class = DemandesDeDepannageSerializer
class NotificationsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DemandesDeDepannage.objects.all()
    serializer_class = DemandesDeDepannageSerializer
    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

#tarifs
class TarifsList(generics.ListCreateAPIView):
    queryset = DemandesDeDepannage.objects.all()
    serializer_class = DemandesDeDepannageSerializer
class TarifsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DemandesDeDepannage.objects.all()
    serializer_class = DemandesDeDepannageSerializer
    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

