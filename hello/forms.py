from django.forms import ModelForm, Textarea, TextInput
from .models import Petition
from django.utils.translation import ugettext_lazy as _


class PetitionForm(ModelForm):
    class Meta:
        model = Petition
        fields = ['title_text','desc_text','improvement','picture']
        widgets = {
            'title_text': TextInput(attrs={'class': 'form-control'}),
            'desc_text': Textarea(attrs={'rows': 6, 'class': 'form-control'}),
            'improvement': Textarea(attrs={'rows': 6, 'class': 'form-control'}),
        }
        labels = {
            'title_text': _('What do you want to achieve?'),
            'desc_text': _('Describe the problem that you want solved'),
            'improvement': _('How your initiative will improve University life?'),
            'picture': _('Add a photo (not required)'),
        }
