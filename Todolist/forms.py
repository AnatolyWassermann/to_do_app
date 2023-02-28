from .models import ToDo
from django import forms

class ToDoForm(forms.Form):
    title = forms.CharField(max_length=100)
    desc = forms.CharField(max_length=500)
    # completed = forms.BooleanField(required=False)

    def save(self):
        data = self.cleaned_data
        todo = ToDo(title=data['title'], 
                    desc=data['desc'], 
                    )
        todo.save()
