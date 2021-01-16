from django import forms
from .models import ProjectUpload

class ProjectUploadForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea(attrs={'rows': 5}))
    class Meta:
        model = ProjectUpload
        fields = '__all__'
