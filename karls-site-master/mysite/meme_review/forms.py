from django import forms
from . models import MemeUpload
#Comment

class MemeUploadForm(forms.ModelForm):
    class Meta():
        model = MemeUpload
        fields = ('user', 'description', 'image')

#class CommentForm(forms.ModelForm):
    #class Meta():
        #model = Comment
        #fields = ('user', 'description')
