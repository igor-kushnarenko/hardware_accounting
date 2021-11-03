from rest_framework import serializers
from base.models import Hardware


class HardwareSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hardware
        fields = ['model', 'serial', 'comment'] # TODO поля с ForeinKey не прикручиваются, разобраться