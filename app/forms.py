from django import forms

class ImageFile(forms.Form):
    image=forms.ImageField()
