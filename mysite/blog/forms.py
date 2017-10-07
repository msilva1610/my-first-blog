from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    pass
    class Meta:
        # temos a classe Meta onde dizemos ao Django qual modelo deveria
        # ser usado para criar este formulário (model = Post).
        model = Post
        fields = ('title', 'text')
