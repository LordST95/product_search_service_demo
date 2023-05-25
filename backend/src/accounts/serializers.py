from rest_framework import serializers

from accounts.models import Member


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        exclude = ['password', 'groups']
        depth = 2
