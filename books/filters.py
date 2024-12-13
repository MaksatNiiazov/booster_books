import django_filters
from .models import Book


class BookFilter(django_filters.FilterSet):
    min_date = django_filters.DateFilter(field_name='published_date', lookup_expr='gte') # >=
    max_date = django_filters.DateFilter(field_name="published_date", lookup_expr='lte') # <=

    class Meta:
        model = Book
        fields = ['title', 'author', 'genre', 'min_date', 'max_date']

