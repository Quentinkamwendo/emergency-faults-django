from django.forms import ModelForm
from .models import Report
from phonenumber_field.widgets import PhoneNumberPrefixWidget


class ReportForm(ModelForm):
    class Meta:
        model = Report
        fields = '__all__'

        widgets = {
             'phone': PhoneNumberPrefixWidget(initial='MW'),
         }
