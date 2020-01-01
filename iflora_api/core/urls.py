from django.urls import path
from iflora_api.core import views

urlpatterns = [
    path('', views.index)
]
