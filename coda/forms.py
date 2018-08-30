from django.forms import ModelForm
from coda.models import Paziente, Priority

class ChangePazientePriorityModelForm(ModelForm):

    def clean_priority(self):
        data = self.cleaned_data['priority_code']
        if data == '':
            raise ValidationError(_('Invalid priority - You must select a priority'))

        return data

    class Meta:
        model = Paziente
        fields = ['priority_code']
