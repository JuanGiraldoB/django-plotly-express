from django import forms
from .models import AudioLabel, FileName


class AudioLabelForm(forms.ModelForm):
    """Form definition for AudioLabel."""

    class Meta:
        """Meta definition for AudioLabelform."""

        model = AudioLabel
        fields = '__all__'


class FileNameForm(forms.ModelForm):
    """Form definition for AudioLabel."""

    class Meta:
        """Meta definition for AudioLabelform."""

        model = FileName
        fields = '__all__'
