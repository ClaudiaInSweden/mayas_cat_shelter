from django.forms import ModelForm
from .models import Cats


class CatsForm(ModelForm):
    class Meta:
        model = Cats
        fields = '__all__'

