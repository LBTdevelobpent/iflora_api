from django.db import models

class BaseModel(models.Model):
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)

class User(BaseModel):
    name= 
    last_name=
    nickname=
    registration= 
    email=
    password= 
    type_user=
    interest=






class Meta:
    abstract= True