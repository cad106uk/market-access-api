from django.conf import settings

from rest_framework import serializers

from api.barriers.models import BarrierInstance
from api.collaboration.models import TeamMember

from api.metadata.constants import (
    ASSESMENT_IMPACT,
    BARRIER_SOURCE,
    BarrierStatus,
    BARRIER_PENDING,
    PROBLEM_STATUS_TYPES,
    TRADE_DIRECTION_CHOICES,
)

from api.metadata.utils import (
    get_admin_area,
    get_country,
    get_sector,
)


class BarrierCsvExportSerializer(serializers.Serializer):
    """ Serializer for CSV export """

    id = serializers.UUIDField()
    code = serializers.CharField()
    scope = serializers.SerializerMethodField()
    status = serializers.SerializerMethodField()
    status_date = serializers.SerializerMethodField()
    summary = serializers.SerializerMethodField()
    barrier_title = serializers.CharField()
    sectors = serializers.SerializerMethodField()
    overseas_region = serializers.SerializerMethodField()
    country = serializers.SerializerMethodField()
    admin_areas = serializers.SerializerMethodField()
    categories = serializers.SerializerMethodField()
    product = serializers.CharField()
    source = serializers.SerializerMethodField()
    priority = serializers.SerializerMethodField()
    team_count = serializers.IntegerField()
    reported_on = serializers.DateTimeField(format="%Y-%m-%d")
    modified_on = serializers.DateTimeField(format="%Y-%m-%d")
    assessment_impact = serializers.SerializerMethodField()
    value_to_economy = serializers.SerializerMethodField()
    import_market_size = serializers.SerializerMethodField()
    commercial_value = serializers.SerializerMethodField()
    export_value = serializers.SerializerMethodField()
    team_count = serializers.SerializerMethodField()
    tags = serializers.SerializerMethodField()
    trade_direction = serializers.SerializerMethodField()
    end_date = serializers.DateField(format="%Y-%m-%d")
    link = serializers.SerializerMethodField()
    economic_assessment_explanation = serializers.SerializerMethodField()
    wto_has_been_notified = serializers.SerializerMethodField()
    wto_should_be_notified = serializers.SerializerMethodField()
    wto_committee_notified = serializers.CharField(
        source="wto_profile.committee_notified.name",
        default="",
    )
    wto_committee_notification_link = serializers.CharField(
        source="wto_profile.committee_notification_link",
        default="",
    )
    wto_member_states = serializers.SerializerMethodField()
    wto_committee_raised_in = serializers.CharField(
        source="wto_profile.committee_raised_in.name",
        default="",
    )
    wto_raised_date = serializers.DateField(
        source="wto_profile.raised_date",
        default="",
        format="%Y-%m-%d",
    )
    wto_case_number = serializers.CharField(
        source="wto_profile.case_number",
        default="",
    )

    class Meta:
        model = BarrierInstance
        fields = (
            "id",
            "code",
            "barrier_title",
            "status",
            "status_date",
            "priority",
            "overseas_region",
            "country",
            "admin_areas",
            "sectors",
            "product",
            "scope",
            "source",
            "team_count",
            "priority",
            "team_count",
            "reported_on",
            "modified_on",
            "assessment_impact",
            "value_to_economy",
            "import_market_size",
            "commercial_value",
            "export_value",
            "end_date",
            "link",
            "economic_assessment_explanation",
        )

    def get_scope(self, obj):
        """  Custom Serializer Method Field for exposing current problem scope display value """
        problem_status_dict = dict(PROBLEM_STATUS_TYPES)
        return problem_status_dict.get(obj.problem_status, "Unknown")

    def get_assessment_impact(self, obj):
        if hasattr(obj, "assessment"):
            impact_dict = dict(ASSESMENT_IMPACT)
            return impact_dict.get(obj.assessment.impact, None)
        return None

    def get_value_to_economy(self, obj):
        if hasattr(obj, "assessment"):
            return obj.assessment.value_to_economy
        return None

    def get_import_market_size(self, obj):
        if hasattr(obj, "assessment"):
            return obj.assessment.import_market_size
        return None

    def get_commercial_value(self, obj):
        if hasattr(obj, "assessment"):
            return obj.assessment.commercial_value
        return None

    def get_export_value(self, obj):
        if hasattr(obj, "assessment"):
            return obj.assessment.export_value
        return None

    def get_status(self, obj):
        """  Custom Serializer Method Field for exposing current status display value """
        status_dict = dict(BarrierStatus.choices)
        sub_status_dict = dict(BARRIER_PENDING)
        status = status_dict.get(obj.status, "Unknown")
        if status == "Open: Pending action":
            status = f"{status} ({sub_status_dict.get(obj.sub_status, 'Unknown')})"
        return status

    def get_status_date(self, obj):
        if obj.status_date:
            return obj.status_date.strftime("%Y-%m-%d")
        else:
            return None

    def get_summary(self, obj):
        if obj.is_summary_sensitive:
            return "OFFICIAL-SENSITIVE (see it on DMAS)"
        else:
            return obj.summary or None

    def get_sectors(self, obj):
        if obj.sectors_affected:
            if obj.all_sectors:
                return "All"
            else:
                sector_names = []
                for sector_id in obj.sectors:
                    sector = get_sector(str(sector_id))
                    if sector and sector.get("name"):
                        sector_names.append(sector.get("name"))
                return sector_names
        else:
            return "N/A"

    def get_country(self, obj):
        country = get_country(str(obj.export_country))
        if country:
            return country.get("name")

    def get_overseas_region(self, obj):
        country = get_country(str(obj.export_country))
        if country:
            overseas_region = country.get("overseas_region")
            if overseas_region:
                return overseas_region.get("name")

    def get_admin_areas(self, obj):
        admin_area_names = []
        for admin_area in obj.country_admin_areas or []:
            admin_area = get_admin_area(str(admin_area))
            if admin_area and admin_area.get("name"):
                admin_area_names.append(admin_area.get("name"))
        return admin_area_names

    def get_categories(self, obj):
        return [category.title for category in obj.categories.all()]

    def get_source(self, obj):
        """  Custom Serializer Method Field for exposing source display value """
        source_dict = dict(BARRIER_SOURCE)
        return source_dict.get(obj.source, "Unknown")

    def get_priority(self, obj):
        """  Custom Serializer Method Field for exposing barrier priority """
        if obj.priority:
            return obj.priority.name
        else:
            return "Unknown"

    def get_team_count(self, obj):
        if hasattr(obj, "team_count"):
            return obj.team_count
        return TeamMember.objects.filter(barrier=obj).count()

    def get_tags(self, obj):
        return [tag.title for tag in obj.tags.all()]

    def get_trade_direction(self, obj):
        if obj.trade_direction:
            trade_directions = dict((str(x), y) for x, y in TRADE_DIRECTION_CHOICES)
            return trade_directions.get(str(obj.trade_direction))
        else:
            return None

    def get_link(self, obj):
        return f"{settings.DMAS_BASE_URL}/barriers/{obj.code}"

    def get_economic_assessment_explanation(self, obj):
        if obj.has_assessment:
            return obj.assessment.explanation
        else:
            return None

    def get_wto_has_been_notified(self, obj):
        if obj.wto_profile:
            if obj.wto_profile.wto_has_been_notified is True:
                return "Yes"
            elif obj.wto_profile.wto_has_been_notified is False:
                return "No"

    def get_wto_should_be_notified(self, obj):
        if obj.wto_profile:
            if obj.wto_profile.wto_should_be_notified is True:
                return "Yes"
            elif obj.wto_profile.wto_should_be_notified is False:
                return "No"

    def get_wto_member_states(self, obj):
        if obj.wto_profile:
            return [
                get_country(str(country_id)).get("name")
                for country_id in obj.wto_profile.member_states
            ]