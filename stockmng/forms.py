from django.forms import ModelForm
from django.forms.formsets import formset_factory
from django.forms.models import modelformset_factory
from django.forms.widgets import CheckboxInput, NumberInput, TextInput
from stockmng.models import Item

# ModelForm For adding new items
class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ['designation', 'price', 'remaining', 'deleteItem']
        widgets = {
            'designation': TextInput(attrs={'class': 'form-control', 'placeholder': 'Designation'}),
            'price': NumberInput(attrs={'class': 'form-control', 'step': '1000', 'min':'0'}),
            'remaining': NumberInput(attrs={'class': 'form-control', 'min': '0'}),
            'deleteItem': CheckboxInput(attrs={'class': 'form-check-input'}),
        }

#ModelFormSet For editing values
ItemFormSet = modelformset_factory(Item, fields = ['designation', 'price', 'remaining', 'deleteItem'],
                                    widgets={'price': NumberInput(attrs={'step': '1000', 'min': '0', 'class': 'form-control form-control-sm'}),
                                    'remaining': NumberInput(attrs={'min': '0', 'class': 'form-control form-control-sm'}),
                                    'designation': TextInput(attrs={'class': 'form-control form-control-sm', 'placeholder': 'Nouveau produit'}),
                                    'deleteItem': CheckboxInput(attrs={'class': 'form-check-input'}),})
                                    
