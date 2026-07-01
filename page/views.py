from django.shortcuts import render
from django.template.defaultfilters import title
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.views import APIView
from page.models import Car, Fifa
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from page.serializers import CarListSerializer, CarCreateSerializer, FifaSerializer


# Create your views here.
class CarAPIView(ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarListSerializer


class CarCreateAPIView(CreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarCreateSerializer


class FifaAPIView(APIView):
    def get(self, request, *args, **kwargs):
        fifa_id = kwargs.get('pk',None)
        if fifa_id:
            fifa = get_object_or_404(Fifa, pk=fifa_id)
            serializer = FifaSerializer(fifa)
            return Response(serializer.data)
        else:
            fifa = Fifa.objects.all()
            serializer = FifaSerializer(fifa, many=True)
            return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = FifaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):
        product_id = kwargs.get('pk')
        product = get_object_or_404(Fifa, pk=product_id)
        serializer = FifaSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, *args, **kwargs):
        product_id = kwargs.get('pk')
        product = get_object_or_404(Fifa, pk=product_id)
        serializer = FifaSerializer(product, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
