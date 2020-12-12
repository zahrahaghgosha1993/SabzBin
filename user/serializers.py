from rest_framework import serializers

from user.models import ProjectUser


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectUser
        fields = ('first_name', 'last_name')


class UserProfileForStaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectUser
        fields = ('first_name', 'last_name','num_addresses')