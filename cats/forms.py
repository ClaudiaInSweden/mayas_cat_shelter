from django.forms import ModelForm
from .models import Cats, Adoption


class CatsForm(ModelForm):
    class Meta:
        model = Cats
        fields = '__all__'
        exclude = ('author',)


class AdoptionForm(ModelForm):
    class Meta:
        model = Adoption
        fields = '__all__'
        exclude = ('cat_id',)
