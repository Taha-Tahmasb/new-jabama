from rest_framework.generics import ListAPIView , CreateAPIView
from .models import Kharidar , Reserve
from django.views.decorators.csrf import csrf_exempt
from django.http.response import HttpResponse, JsonResponse
from . serializer import ReserverSerializer , KharidarSerializer
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from rest_framework.permissions import IsAuthenticated


class Login(TokenObtainPairView):
    pass

class Refresh(TokenRefreshView):
    pass


class MyReserves(ListAPIView):
    queryset = Reserve.objects.all()
    serializer_class = ReserverSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Reserve.objects.filter(Kharidar = self.request.user)
    


class NewReserve(CreateAPIView):
    queryset = Reserve.objects.all()
    serializer_class = ReserverSerializer
    permission_classes = [IsAuthenticated]



    






