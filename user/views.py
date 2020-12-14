from rest_framework.generics import ListAPIView
from django_filters import rest_framework as filters

from user.filters import UserFilter
from user.models import ProjectUser
from user.serializers import UserProfileForStaffSerializer


class UserListAPIView(ListAPIView):
    serializer_class = UserProfileForStaffSerializer
    queryset = ProjectUser.with_addresses_count_objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = UserFilter
