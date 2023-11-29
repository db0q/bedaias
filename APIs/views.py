from django.shortcuts import render
from django.shortcuts import render,get_object_or_404
from rest_framework import generics, response,status
from .models import *
from .serializers import *
from django.views import View
from django.http import JsonResponse
from rest_framework.views import APIView
from . models import *
from rest_framework.response import Response

# Create your views here.
class BedaiaListAPIView(generics.ListAPIView):
    serializer_class = BedaiaSerializer

    def get_queryset(self):
        return Bedaia.objects.all()


class BedaiaDetailsAPIView(generics.GenericAPIView):
    serializer_class = BedaiaSerializer

    def get(self,request,slug):
        query_set = Bedaia.objects.filter(slug=slug).first()

        if query_set:
            return response.Response(self.serializer_class(query_set).data)
        return response.Response('not found', status=status.HTTP_404_NOT_FOUND)
class NukhbaListAPIView(generics.ListAPIView):
    serializer_class = NukhbaSerializer

    def get_queryset(self):
        return Nukhba.objects.all()


class NukhbaDetailsAPIView(generics.GenericAPIView):
    serializer_class = NukhbaSerializer

    def get(self,request,slug):
        query_set = Nukhba.objects.filter(slug=slug).first()

        if query_set:
            return response.Response(self.serializer_class(query_set).data)
        return response.Response('not found', status=status.HTTP_404_NOT_FOUND)


# Create your views here.
