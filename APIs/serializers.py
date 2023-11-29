from rest_framework import serializers
from . models import *


class BedaiaSerializer(serializers.ModelSerializer):
   
    class Meta:
        model=Bedaia
        fields="__all__"

class NukhbaSerializer(serializers.ModelSerializer):
   
    class Meta:
        model=Nukhba
        fields="__all__"





