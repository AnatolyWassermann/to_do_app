from django.contrib.auth.models import User
import datetime
from mongoengine import (Document, 
                         StringField, 
                         BooleanField, 
                         DateTimeField,
                         IntField)



class ToDo(Document):
    title = StringField(required=True, max_length=100)
    desc = StringField(max_length=500)
    user = IntField(required=True)
    slug = StringField()
    completed = BooleanField(default=False)
    created = DateTimeField(default=datetime.datetime.utcnow)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.title.replace(' ', '-')
        return super(ToDo, self).save(*args, **kwargs)
