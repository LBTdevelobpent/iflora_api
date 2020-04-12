from django.db import models

class BaseModel(models.Model):
    '''
     Generic class to the database.
    '''

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class User(BaseModel):
    '''
     Model class for users
    '''

    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=8)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=170)
    bio = models.CharField(max_length=700)
    profile_pic = models.CharField(max_length=700)

class CommonUser(User):
    '''
     Model for common users inside us system
    '''

    cpf = models.CharField(max_length=14)

class Student(User):
    '''
     Model for students users
    '''

    registration = models.CharField(max_length=14)

class Teacher(User):
    '''
     Model for teachers users
    '''

    registration = models.CharField(max_length=50)
    school_subject = models.CharField(max_length=50)

class Categories(BaseModel):
    '''
    Model to list the possibles categories to the types of events.
    '''

    title = models.CharField(max_length=170, null=False)
    text = models.CharField(max_length=250, null=False)
    id = models.AutoField(primary_key=True)


class Post(BaseModel):
    '''
    Model for save posts
    '''
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, null=False)
    text = models.CharField(max_length=300, null=False)
    posted_by = models.CharField(max_length=170) # UPDATE TO FOREIGN KEY WITH USER
    like = models.IntegerField(default=0)
    denunciations = models.IntegerField(default=0)
    #comments = models.ArrayField(Comment, default=[])

class Post_Categorie(BaseModel):
    '''
    Model to connect the Posts with their categories
    '''
    #post_id = models.ForeignKey(Post, related_name='id')
    #categorie_id = models.ForeignKey(Categories, related_name='id')

    #class Meta:
        #id = (('post_id', 'categorie_id'))

class Event(Post):

    date = models.DateField(null=False)
    place = models.CharField(null=False, max_length=300)
    time_duration = models.TimeField()
    confirmed = models.IntegerField(default=0)

class Comment(BaseModel):
    text = models.CharField(max_length=200, null=False)
    posted_by = models.CharField(max_length=50)     #UPDATE TO USER FOREIGN KEY
    like = models.IntegerField(default=0)
    #post_id = models.ForeignKey(Post)

