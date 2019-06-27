from django import forms

from dashboard.models import Company


def get_model_choices():
    choices_list = []
    for company in Company.objects.all():
        choices_list.append((company.name, company.name))

    return choices_list


class DashboardQueryForm(forms.Form):
    company_name = forms.ChoiceField(label="Company Name", choices=get_model_choices())
    from_date = forms.DateField(label='Start Date', widget=forms.SelectDateWidget)
    to_date = forms.DateField(label='End Date', widget=forms.SelectDateWidget)