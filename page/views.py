from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.generics import ListAPIView, CreateAPIView

from page.models import Car
from page.serializers import CarListSerializer, CarCreateSerializer


# Create your views here.
class CarAPIView(ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarListSerializer


class CarCreateAPIView(CreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarCreateSerializer