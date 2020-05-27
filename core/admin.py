from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(User)
admin.site.register(CommonUser)
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Categories)
admin.site.register(Post)
admin.site.register(Post_Categorie)
admin.site.register(Event)
admin.site.register(Comment)
