from django import forms
from .models import NewPost

class PostForm(forms.ModelForm):
    class Meta:
        model = NewPost
        fields = ['post',]

        widgets = {
            'post' : forms.Textarea(attrs={
                'class' : "form-control",
                'placeholder': "What is in your mind?",
                'rows' : 4,
                'cols' : 10
            })
        }

        labels = {
            'post' : ''
        }