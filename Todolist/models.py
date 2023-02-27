from django.db import models
import datetime
from mongoengine import Document, StringField, BooleanField, DateTimeField

class ToDo(Document):
    title = StringField(required=True, max_length=100)
    desc = StringField(max_length=500)
    completed = BooleanField()
    created = DateTimeField(default=datetime.datetime.utcnow)
    
    def __str__(self):
        return self.title

# Create your models here.
