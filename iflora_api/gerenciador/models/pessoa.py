from django.db import models
from .base_model import BaseModel

class Pessoa(BaseModel):
    nome= models.CharField(max_length=50) 
    nickname= models.CharField(max_lenght=155)
    email= models.EmailField(max_length=254)
    senha= models.CharField(max_length=8)
    bio= models.CharField(_(max_length=500)
    