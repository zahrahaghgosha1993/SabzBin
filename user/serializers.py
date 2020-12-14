from rest_framework import serializers

from user.models import ProjectUser


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectUser
        fields = ('uid','first_name', 'last_name')


class UserProfileForStaffSerializer(serializers.ModelSerializer):
    num_addresses = serializers.IntegerField()
    class Meta:
        model = ProjectUser
        fields = ('uid' ,'first_name', 'last_name','num_addresses')