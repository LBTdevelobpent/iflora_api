from django.db import models

class BaseModel(models.Model):
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)

class User(models.Model):
    name= models.CharField(max_length=240, null=True)
    last_name= models.CharField(max_length=240, null=True)
    nickname= models.CharField(max_length=240, null=True)
    registration= models.CharField(max_length=10, null=True)
    email= models.EmailField(max_length=240, null=True)
    bio= models.CharField(max_length=620, null=True)
    password= models.CharField(max_length=8, null=True)

    PROFESSOR= 'PR'
    ALUNO= 'AL'
    TYPE_USER_CHOICES= [
        (PROFESSOR, 'Professor'),
        (ALUNO, 'Aluno'),
    ]
    type_user= models.CharField(max_length=2,choices=TYPE_USER_CHOICES,default=ALUNO,)

    TECNOLOGIA= 'TE'
    ARTE= 'AR'
    INTEREST_CHOICES= [
        (TECNOLOGIA, 'Tecnologia'),
        (ARTE, 'Arte'),
    ]
    interest= models.CharField(max_length=2,choices=INTEREST_CHOICES,default=TECNOLOGIA,)
'''
class Post(User):
    title=
    likes=
    description=
    media=

class Event(User):
    title=
    description=
    location=
    date=
    hour=
    duration=
    category=
    likes=
    media=

class Comment(User):
    text=
    likes=
'''
class Meta:
    abstract= True