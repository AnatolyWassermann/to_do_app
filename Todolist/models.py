from django.db import models
from mongoengine import Document, StringField

class ToDo(Document):
    title = StringField(required=True, max_length=100)
    desc = StringField(required=False, max_length=500)

# Create your models here.
