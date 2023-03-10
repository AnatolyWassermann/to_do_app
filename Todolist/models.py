
import datetime
import random
from mongoengine import (Document, 
                         StringField, 
                         BooleanField, 
                         DateTimeField,
                         IntField)
import django.utils.text import slugify

def random_string_generator(size=5, chars = string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))

class ToDo(Document):
    title = StringField(max_length=100, required=True)
    desc = StringField()
    user = IntField(required=True)
    slug = StringField()
    completed = BooleanField(default=False)
    created = DateTimeField(default=datetime.datetime.utcnow)
    
    meta = {
        'ordering': ['-created']
    }
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        
        if not self.slug:
            self.slug = slugify(self.title) + random_string_generator(size=5)
            

        return super(ToDo, self).save(*args, **kwargs)
