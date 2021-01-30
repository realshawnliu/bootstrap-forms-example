from django.urls import path

from search.views import SearchCreateView


urlpatterns = [
    path('', SearchCreateView.as_view(), name='search_view'),
]
