from .models import Forooshandeh , Ja
from rest_framework.serializers import ModelSerializer



class JaSerializer(ModelSerializer):
    class Meta:
        model = Ja
        fields = '__all__'


class ForoooshandehSerializer(ModelSerializer):
    class Meta:
        model = Forooshandeh
        fields ='__all__'


