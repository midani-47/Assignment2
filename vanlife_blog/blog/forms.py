from django import forms
from .models import Post, Journey, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model =Post
        fields= ('title', 'content', 'location')

class JourneyForm(forms.ModelForm):
    class Meta:
        model=Journey
        fields= ('title', 'description', 'start_date', 'end_date')

class CommentForm(forms.ModelForm):
    class Meta:
        model= Comment
        fields= ('text',)
#
#