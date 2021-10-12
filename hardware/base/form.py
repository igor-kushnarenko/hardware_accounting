from django import forms

from .models import Hardware, Repair


class HardwareForm(forms.ModelForm):
    class Meta:
        model = Hardware
        fields = '__all__'


class RepairForm(forms.ModelForm):
    class Meta:
        model = Repair
        fields = ['date_repair', 'problem', 'contractor', 'end_date_repair', 'result', 'cost', 'status']
