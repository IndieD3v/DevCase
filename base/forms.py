from django import forms
from .models import Projects

class NewProject(forms.ModelForm):

    class Meta:
        model = Projects
        fields = ['project_name','url','image','description']


        widgets = {
            'project_name': forms.TextInput(attrs={'placeholder':'Project Name'}),
            'url': forms.TextInput(attrs={'placeholder':'URL'}),
            'description': forms.Textarea(attrs={'placeholder':'Description'}),
        }