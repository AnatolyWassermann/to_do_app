
import datetime
import random
import unicodedata
import string
import re
from mongoengine import (Document, 
                         StringField, 
                         BooleanField, 
                         DateTimeField,
                         IntField)

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
        ''' since slugify function doesn't support mongoengine i customized it a bit '''
        if not self.slug:
            # self.slug = self.title.replace(' ', '-') + random_slug_generator(size=10)
            current_title = str(self.title)
            current_title = (
                unicodedata.normalize("NFKD", current_title)
                .encode('ascii', 'ignore')
                .decode('ascii')
            )
            current_title = re.sub(r"[^\w\s-]", "", current_title.lower())
            current_title = re.sub(r"[-\s]+", "-", current_title).strip("-_")
            self.slug = current_title + random_string_generator(size=5)

        return super(ToDo, self).save(*args, **kwargs)
