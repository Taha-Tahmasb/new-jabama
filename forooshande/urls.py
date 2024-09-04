from django.urls import path
from .views import NewJa , AllJa , MyJa


urlpatterns = [
    path("myja/" , MyJa.as_view()),
    path("allja/" , AllJa.as_view()),
    path("newja/" , NewJa.as_view()),
]