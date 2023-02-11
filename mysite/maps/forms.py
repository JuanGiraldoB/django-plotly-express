from django import forms
from .models import AudioLabel


class AudioLabelForm(forms.ModelForm):
    """Form definition for AudioLabel."""

    class Meta:
        """Meta definition for AudioLabelform."""

        model = AudioLabel
        fields = '__all__'
