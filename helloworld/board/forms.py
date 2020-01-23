from .models import Topic
from django import forms

class NewTopicForm(forms.ModelForm):
    message = forms.CharField(
        widget = forms.Textarea(
            attrs = {'rows': 5, 'placeholder': 'Write your thoughts...'}
        ), 
        max_length = 4000,
        help_text = 'The Max Length is 4000!')

    class Meta:
        model = Topic
        fields = ['subject', 'message']
