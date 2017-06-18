from django import forms
from .models import Post


class BlogPostForm(forms.ModelForm):
    # Create a Blog Form options
    class Meta:
        model = Post
        fields = ('title', 'content', 'image')
