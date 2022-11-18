from django import forms
from .models import Post
from .models import Test
# from .models import UploadImage

# class PostForm(forms.ModelForm):
#     class Meta:
#         model = Post
#         fields = ["title", "slug", "intro", "body"]

class PostForm(forms.Form):
    title = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder':'タイトル'}))
    slug = forms.SlugField()
    intro = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'概要'}))
    body = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'入力してください'}), max_length=100)
    img = forms.CharField(required=False)
    # data_added = forms.DateTimeField(auto_now_add=True)
    
# class UploadForm(forms.ModelForm):
#     class Meta:
#         model = UploadImage
#         fields = ['image']

class TestForm(forms.Form):
    test_title = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder':'タイトル'}))