from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from search.models import Search


class SearchForm(forms.ModelForm):
    class Meta:
        model = Search
        fields = ('domain', 'keyword', 'start_date', 'end_date')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Search'))
