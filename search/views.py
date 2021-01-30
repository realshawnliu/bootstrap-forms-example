from django.views.generic import CreateView
from django.urls import reverse_lazy

from search.models import Search
from search.forms import SearchForm


class SearchCreateView(CreateView):
    model = Search
    fields = ('domain', 'keyword', 'start_date', 'end_date')
    success_url = reverse_lazy('search_view')
