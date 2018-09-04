
from rest_framework import serializers

from api.barriers.models import (
    BarrierContributor,
    BarrierInstance,
    BarrierInteraction,
    BarrierStatus
)
from api.metadata.constants import STAGE_STATUS

# pylint: disable=R0201

class BarrierReportStageListingField(serializers.RelatedField):
    def to_representation(self, value):
        stage_status_dict = dict(STAGE_STATUS)
        return {
            "stage_code": value.stage.code,
            "stage_desc": value.stage.description,
            "status_id": value.status,
            "status_desc": stage_status_dict[value.status],
        }


class BarrierReportSerializer(serializers.ModelSerializer):
    progress = BarrierReportStageListingField(many=True, read_only=True)

    class Meta:
        model = BarrierInstance
        fields = (
            "id",
            "problem_status",
            "is_resolved",
            "resolved_date",
            "export_country",
            "sectors_affected",
            "sectors",
            "product",
            "source",
            "other_source",
            "barrier_title",
            "problem_description",
            "barrier_type",
            "progress"
        )
        read_only_fields = ("id", "progress", "created_on")


class BarrierListSerializer(serializers.ModelSerializer):
    """ Serializer for listing Barriers """
    current_status = serializers.SerializerMethodField()
    contributor_count = serializers.SerializerMethodField()
    reported_by = serializers.SerializerMethodField()

    class Meta:
        model = BarrierInstance
        fields = (
            "id",
            "reported_on",
            "reported_by",
            "problem_status",
            "is_resolved",
            "barrier_title",
            "export_country",
            "contributor_count",
            "current_status"
        )

    def get_reported_by(self, obj):
        return obj.created_by.email if obj.created_by else ""

    def get_current_status(self, obj):
        """  Custom Serializer Method Field for exposing current barrier status as json """
        # barrier_status = BarrierStatus.objects.filter(barrier=obj).latest("created_on")
        return {
            "status": obj.status,
            "status_date": obj.status_date,
            "summary": obj.summary,
        }

    def get_contributor_count(self, obj):
        """ Custom Serializer Method Field for barrier count """
        barrier_contributors_count = BarrierContributor.objects.filter(
            barrier=obj,
            is_active=True
        ).count()
        return barrier_contributors_count


class BarrierResolveSerializer(serializers.ModelSerializer):
    """ Serializer for resolving a barrier """
    class Meta:
        model = BarrierStatus
        fields = (
            "id",
            "barrier",
            "status",
            "status_date",
            "summary",
            "is_active",
            "created_on",
            "created_by"
        )
        read_only_fields = ("id", "status", "barrier", "is_active", "created_on", "created_by")


class BarrierStaticStatusSerializer(serializers.ModelSerializer):
    """ generic serializer for other barrier statuses """
    class Meta:
        model = BarrierStatus
        fields = (
            "id",
            "barrier",
            "status",
            "status_date",
            "summary",
            "is_active",
            "created_on",
            "created_by"
        )
        read_only_fields = (
            "id",
            "status",
            "barrier",
            "status_date",
            "is_active",
            "created_on",
            "created_by"
        )


class BarrierInstanceSerializer(serializers.ModelSerializer):
    """ Serializer for Barrier Instance """
    current_status = serializers.SerializerMethodField()
    report = serializers.SerializerMethodField()

    class Meta:
        model = BarrierInstance
        fields = (
            "id",
            "barrier_type",
            "summary",
            "chance_of_success",
            "chance_of_success_summary",
            "estimated_loss_range",
            "impact_summary",
            "other_companies_affected",
            "has_legal_infringement",
            "wto_infringement",
            "fta_infringement",
            "other_infringement",
            "infringement_summary",
            "report",
            "reported_on",
            "created_on",
            "created_by",
            "current_status"
        )
        depth = 1

    def get_current_status(self, obj):
        return {
            "status": obj.status,
            "status_date": obj.status_date,
            "summary": obj.summary,
        }

    def get_report(self, obj):
        return {
            "id": obj.report.id,
            "problem_status": obj.report.problem_status,
            "is_emergency": obj.report.is_emergency,
            "company": {
                "id": obj.report.company_id,
                "name": obj.report.company_name,
                "sector_id": obj.report.company_sector_id,
                "sector_name": obj.report.company_sector_name,
                "contact_id": obj.report.contact_id,
            },
            "product": obj.report.product,
            "commodity_codes": obj.report.commodity_codes,
            "export_country": obj.report.export_country,
            "problem_description": obj.report.problem_description,
            "barrier_title": obj.report.barrier_title,
            "problem_impact": obj.report.problem_impact,
            "estimated_loss_range": obj.report.estimated_loss_range,
            "other_companies_affected": obj.report.other_companies_affected,
            "other_companies_info": obj.report.other_companies_info,
            "has_legal_infringement": obj.report.has_legal_infringement,
            "wto_infringement": obj.report.wto_infringement,
            "fta_infringement": obj.report.fta_infringement,
            "other_infringement": obj.report.other_infringement,
            "infringement_summary": obj.report.infringement_summary,
            "is_resolved": obj.report.is_resolved,
            "resolved_date": obj.report.resolved_date,
            "resolution_summary": obj.report.resolution_summary,
            "support_type": obj.report.support_type,
            "steps_taken": obj.report.steps_taken,
            "is_politically_sensitive": obj.report.is_politically_sensitive,
            "political_sensitivity_summary": obj.report.political_sensitivity_summary,
            "govt_response_requested": obj.report.govt_response_requested,
            "is_commercially_sensitive": obj.report.is_commercially_sensitive,
            "commercial_sensitivity_summary": obj.report.commercial_sensitivity_summary,
            "can_publish": obj.report.can_publish,
            "created_on": obj.report.created_on,
            "status": obj.report.status,
            "barrier_type": obj.report.barrier_type.id,
            "created_by": obj.report.created_by.email if obj.report.created_by else "",
        }

class BarrierInteractionSerializer(serializers.ModelSerializer):
    """ Serialzer for Barrier Ineractions """
    class Meta:
        model = BarrierInteraction
        fields = "__all__"
        read_only_fields = ("barrier", "kind", "created_on", "created_by")


class BarrierContributorSerializer(serializers.ModelSerializer):
    """ Serializer for Barrier Contributors """
    class Meta:
        model = BarrierContributor
        fields = "__all__"
        read_only_fields = ("barrier", "created_on", "created_by")
