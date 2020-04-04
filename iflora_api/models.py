from django.db import models

class BaseModel(models.Model):
    '''
     Generic class to the database.
    '''

    created_at = models.DateField();
    updated_at = models.DateField();
