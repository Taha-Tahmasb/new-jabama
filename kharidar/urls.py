from django.urls import path
from .views import MyReserves , NewReserve , Login


urlpatterns = [
    path("login/" , Login.as_view()),
    path("new_reserve/" , NewReserve.as_view()),
    path("my_reserve/" , MyReserves.as_view()),
]