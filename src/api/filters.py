from django_filters import rest_framework as filters
from django.db.models import Q

from api.models import Product


class NumberInFilter(filters.BaseInFilter, filters.NumberFilter):
    pass


class ProductFilter(filters.FilterSet):

    class Meta:
        model = Product
        fields = ['name']
    
    category = filters.CharFilter(lookup_expr='icontains')
    brand = filters.CharFilter(lookup_expr='icontains')
    price__gte = filters.NumberFilter(field_name='price', lookup_expr='gte')
    price__lte = filters.NumberFilter(field_name='price', lookup_expr='lte')
    quantity__gte = filters.NumberFilter(field_name='quantity', lookup_expr='gte')
    quantity__lte = filters.NumberFilter(field_name='quantity', lookup_expr='lte')
    def created_at_filter(queryset, name, value):
        """
        the format of 'created_at' should be sth like: ?created_at=2023-05-25 instead of 2023-05-25T15:54:39.212653Z
        """
        queryset = queryset.filter(created_at__date=value)
        return queryset
    created_at = filters.CharFilter(field_name="created_at", method=created_at_filter)
    # created_at = filters.DateTimeFilter(field_name='created_at')  # format: 2023-05-25T15:54:39.212653Z
    def rating_filter(queryset, name, value):
        """
        the format of 'rating' should be sth like: 1 or 1,2,5
        """
        query = Q()
        for rate in value.split(","):
            query |= Q(rating=float(rate))
        queryset = queryset.filter(query)
        return queryset
    rating = filters.CharFilter(field_name='rating', method=rating_filter)
