from django import forms
from .models import Watch



class WatchForm(forms.ModelForm):
    class Meta:
        model = Watch
        # fields = ["name",'price','year','img']
        fields='__all__'
        widgets = {
            'brand': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.TextInput(attrs={'class': 'form-control'}),
            

        }
        widgets['image'] = forms.ClearableFileInput(attrs={'class': 'form-control-file'})
