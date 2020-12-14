from django_filters import rest_framework as filters

from user.models import ProjectUser


class UserFilter(filters.FilterSet):
    min_address_count = filters.NumberFilter(field_name="num_addresses", lookup_expr='gte')
    max_address_count = filters.NumberFilter(field_name="num_addresses", lookup_expr='lte')

    class Meta:
        model = ProjectUser
        fields = ['min_address_count', 'max_address_count']
