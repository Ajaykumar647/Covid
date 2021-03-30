from rest_framework import  serializers
from .models import HospitalModel

class HospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = HospitalModel
        fields = "__all__"