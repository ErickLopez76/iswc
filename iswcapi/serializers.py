from rest_framework import serializers

from iswcsview.models import Iswc

class IswcSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Iswc
        fields = ('title', 'contributors')

class IswcSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Iswc
        fields = ('iswc', 'title', 'contributors')