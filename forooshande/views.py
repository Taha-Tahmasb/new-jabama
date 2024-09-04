from rest_framework.generics import ListAPIView , CreateAPIView
from .serializer import JaSerializer , ForoooshandehSerializer
from . models import Ja , Forooshandeh
from rest_framework.permissions import IsAuthenticated


class NewJa(CreateAPIView):
    queryset = Ja.objects.all()
    serializer_class = JaSerializer
    permission_classes = [IsAuthenticated]


class AllJa(ListAPIView):
    queryset = Ja.objects.all()
    serializer_class = JaSerializer


class MyJa(ListAPIView):
    queryset = Forooshandeh.objects.all()
    serializer_class = ForoooshandehSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Forooshandeh.objects.filter(user = self.request.user)
    

