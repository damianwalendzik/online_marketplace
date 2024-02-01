from django import forms

from .models import ConversationMessage

class ConversationMessage(forms.ModelForm):
    class Meta:
        