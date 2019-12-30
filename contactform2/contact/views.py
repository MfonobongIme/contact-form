from django.shortcuts import render
from rest_framework import viewsets
from .models import contact
from .serializers import contactSerializer

# Create your views here.
class contactView(viewsets.ModelViewSet):
	queryset = contact.objects.all()
	serializer_class = contactSerializer

