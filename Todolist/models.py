
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
    desc = StringField(max_length=500)
    user = IntField(required=True)
    slug = StringField()
    completed = BooleanField(default=False)
    created = DateTimeField(default=datetime.datetime.utcnow)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        ''' since slugify function doesn't support mongoengine i customized it a bit '''
        if not self.slug:
            # self.slug = self.title.replace(' ', '-') + random_slug_generator(size=10)
            title = str(self.title)
            title = (
                unicodedata.normalize("NFKD", title)
                .encode('ascii', 'ignore')
                .decode('ascii')
            )
        title = re.sub(r"[^\w\s-]", "", title.lower())
        title = re.sub(r"[-\s]+", "-", title).strip("-_")
      
        self.slug = title + random_string_generator(size=5)

        return super(ToDo, self).save(*args, **kwargs)
