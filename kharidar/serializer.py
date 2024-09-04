from .models import Reserve , Kharidar
from rest_framework.serializers import ModelSerializer


class ReserverSerializer(ModelSerializer):
    class Meta:
        model = Reserve
        fields = '__all__'


class KharidarSerializer(ModelSerializer):
    class Meta:
        model = Kharidar
        fields = '__all__'

