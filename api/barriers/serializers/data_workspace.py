from rest_framework import serializers

from api.collaboration.models import TeamMember
from .base import BarrierSerializerBase


class DataWorkspaceSerializer(BarrierSerializerBase):
    team_count = serializers.SerializerMethodField()

    class Meta(BarrierSerializerBase.Meta):
        fields = (
            "admin_areas",
            "assessment",
            "all_sectors",
            "archived",
            "archived_by",
            "archived_explanation",
            "archived_on",
            "archived_reason",
            "categories",
            "code",
            "commodities",
            "companies",
            "country",
            "created_by",
            "created_on",
            "end_date",
            "has_assessment",
            "id",
            "is_summary_sensitive",
            "modified_by",
            "modified_on",
            "other_source",
            "priority",
            "priority_summary",
            "product",
            "public_barrier",
            "public_eligibility",
            "public_eligibility_summary",
            "sectors",
            "sectors_affected",
            "source",
            "status",
            "status_date",
            "status_summary",
            "sub_status",
            "sub_status_other",
            "summary",
            "tags",
            "team_count",
            "term",
            "title",
            "trade_direction",
            "unarchived_by",
            "unarchived_on",
            "unarchived_reason",
            "wto_profile",
        )

    def get_team_count(self, obj):
        return TeamMember.objects.filter(barrier=obj).count()