from django import forms
from .models import Task
from datetime import date

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'status']

    def clean_due_date(self):
        due_date = self.cleaned_data['due_date']
        
        if self.instance.pk is None and due_date < date.today():
            raise forms.ValidationError("Due date cannot be in the past.")
        
        return due_date

