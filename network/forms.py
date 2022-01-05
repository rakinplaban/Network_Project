from django import forms

from .models import NewPost

class NewPostForm(forms.ModelForm):
    class Meta:
        model = NewPost
        fields = ["post",]

        widgets = {
            'post' : forms.Textarea(attrs={
                "class" : "form-control",
                "placeholder" : "What's in your mind?",
                "cols" : 30,
                "rows" : 3
            })
        }

        labels = {
            'post' : ''
        }