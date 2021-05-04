from django import forms
from .models import Comment


class PizzaComment(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["comment"]
        labels = {"comment": ""}
