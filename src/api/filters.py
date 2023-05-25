from django_filters import rest_framework as filters

from api.models import Product


class NumberInFilter(filters.BaseInFilter, filters.NumberFilter):
    pass


class ProductFilter(filters.FilterSet):

    class Meta:
        model = Product
        fields = ['category', 'brand']
        
    price__gte = filters.NumberFilter(field_name='price', lookup_expr='gte')
    price__lte = filters.NumberFilter(field_name='price', lookup_expr='lte')
    quantity__gte = filters.NumberFilter(field_name='quantity', lookup_expr='gte')
    quantity__lte = filters.NumberFilter(field_name='quantity', lookup_expr='lte')
    def created_at_filter(queryset, name, value):
        """
        the format of 'created_at' should be sth like: ?created_at=2023-05-25 instead of 2023-05-25T15:54:39.212653Z
        """
        # year, month, day = str(value).split("-")
        queryset = queryset.filter(created_at__date=value)
        return queryset
    created_at = filters.CharFilter(field_name="created_at", method=created_at_filter)
    # created_at = filters.DateTimeFilter(field_name='created_at')  # format: 2023-05-25T15:54:39.212653Z
    rating = filters.NumberFilter(field_name='rating', lookup_expr='in')
