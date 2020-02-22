from django import forms
from .models import Topic

class TopicForm(forms.ModelForm):
    """Form to collect/display data about a specific topic."""
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}