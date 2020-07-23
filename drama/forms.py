from django import forms

from drama.models import Project


class DramaModelForm(forms.ModelForm):
    _CHANNELS = (('0', 'KBS'), ('1', 'SBS'), ('2', 'MBC'), ('3', 'tvN'))
    _WEEKS = (('0', '월·화'), ('1', '수·목'), ('2', '금·토'), ('3', '토·일'))
    channel = forms.ChoiceField(widget=forms.Select, choices=_CHANNELS, initial=0)
    week = forms.ChoiceField(widget=forms.Select, choices=_WEEKS, initial=0)

    class Meta:
        model = Project
        fields = ['title', 'round', 'channel', 'week', 'diary', 'img', 'video']