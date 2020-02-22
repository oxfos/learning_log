from django import forms
from .models import Topic, Entry

class TopicForm(forms.ModelForm):
    """Form to collect/display data about a specific topic."""
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}

class EntryForm(forms.ModelForm):
    """Form to register an entry."""
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': 'Entry:'}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}