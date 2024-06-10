from django import forms
from core.models import NotesUpload

class notesUploadForm(forms.ModelForm):
    class Meta:
        model = NotesUpload
        fields = ('title', 'note')
