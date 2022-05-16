from django.shortcuts import render
from rest_framework import viewsets

from .serializers import IswcSerializer
from iswcsview.models import Iswc


class IswcViewSet(viewsets.ModelViewSet):
    queryset = Iswc.objects.all().order_by('title')
    serializer_class = IswcSerializer