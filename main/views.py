from django.shortcuts import render
from main.models import Portfolio
from main.serializers import PortfolioSerializer
from rest_framework import viewsets
from .models import Portfolio

# Create your views here.

class PortfolioViewSet(viewsets.ModelViewSet):
   queryset = Portfolio.objects.all()
   serializer_class = PortfolioSerializer
