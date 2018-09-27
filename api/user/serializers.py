from rest_framework import serializers

from django.contrib.auth import get_user_model

UserModel = get_user_model()


class WhoAmISerializer(serializers.ModelSerializer):
    """User serializer"""

    location = serializers.SerializerMethodField()

    class Meta:
        model = UserModel
        fields = (
            "id",
            "username",
            "last_login",
            "first_name",
            "last_name",
            "email",
            "location",
        )

    def get_location(self, obj):
        return obj.profile.location if obj.profile else None
