from .models import CoinName
from django.forms import ModelForm, TextInput


class CoinForm(ModelForm):
    class Meta:
        model = CoinName
        fields = ['name']
        widgets = {'name': TextInput(attrs={'class': 'form-control', 'name': 'city', 'id': 'coin',
                                            'placeholder': 'Enter coin'})}
