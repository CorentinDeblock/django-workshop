from . import views
from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea({'class':"form-control w-100",'rows':5,'placeholder':'content'}),label='')
    class Meta:
        model = Post
        fields = ['username','photo','content']