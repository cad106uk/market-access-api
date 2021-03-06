from hashid_field.rest import HashidSerializerCharField
from rest_framework import serializers

from api.barriers.fields import (
    NoneToBlankCharField,
    ReadOnlyStatusField,
    ReadOnlyCountryField,
    ReadOnlySectorsField,
    ReadOnlyAllSectorsField,
    ReadOnlyCategoriesField,
    ReadOnlyTradingBlocField,
)
from api.barriers.helpers import get_published_public_barriers
from api.barriers.models import PublicBarrier
from api.barriers.serializers.mixins import LocationFieldMixin
from api.core.serializers.mixins import AllowNoneAtToRepresentationMixin
from api.interactions.models import PublicBarrierNote
from api.interactions.serializers import PublicBarrierNoteSerializer
from api.metadata.fields import TradingBlocField


PUBLIC_ID = "barriers.PublicBarrier.id"


class NestedPublicBarrierSerializer(serializers.ModelSerializer):
    """
    Simple serializer for use within BarrierDetailSerializer.
    """
    class Meta:
        model = PublicBarrier
        fields = (
            "public_view_status",
        )


class PublicBarrierSerializer(AllowNoneAtToRepresentationMixin,
                              serializers.ModelSerializer):
    """
    Generic serializer for barrier public data.
    """
    id = HashidSerializerCharField(source_field=PUBLIC_ID, read_only=True)
    title = NoneToBlankCharField()
    summary = NoneToBlankCharField()
    internal_title_changed = serializers.SerializerMethodField()
    internal_summary_changed = serializers.SerializerMethodField()
    status = ReadOnlyStatusField()
    internal_status = ReadOnlyStatusField()
    country = ReadOnlyCountryField()
    internal_country = ReadOnlyCountryField()
    trading_bloc = TradingBlocField()
    internal_trading_bloc = TradingBlocField()
    sectors = ReadOnlySectorsField()
    internal_sectors = ReadOnlySectorsField()
    all_sectors = ReadOnlyAllSectorsField()
    internal_all_sectors = ReadOnlyAllSectorsField()
    categories = ReadOnlyCategoriesField()
    internal_categories = ReadOnlyCategoriesField()
    latest_published_version = serializers.SerializerMethodField()
    unpublished_changes = serializers.SerializerMethodField()
    ready_to_be_published = serializers.SerializerMethodField()
    internal_code = serializers.SerializerMethodField()
    internal_id = serializers.SerializerMethodField()
    latest_note = serializers.SerializerMethodField()
    reported_on = serializers.DateTimeField(source="internal_created_on")

    class Meta:
        model = PublicBarrier
        fields = (
            "id",
            "internal_code",
            "internal_id",
            "title",
            "title_updated_on",
            "internal_title_changed",
            "internal_title_at_update",
            "summary",
            "summary_updated_on",
            "internal_summary_changed",
            "internal_summary_at_update",
            "status",
            "internal_status",
            "internal_status_changed",
            "status_date",
            "internal_status_date",
            "internal_status_date_changed",
            "is_resolved",
            "internal_is_resolved",
            "internal_is_resolved_changed",
            "country",
            "internal_country",
            "internal_country_changed",
            "trading_bloc",
            "internal_trading_bloc",
            "internal_trading_bloc_changed",
            "location",
            "internal_location",
            "internal_location_changed",
            "sectors",
            "internal_sectors",
            "internal_sectors_changed",
            "all_sectors",
            "internal_all_sectors",
            "internal_all_sectors_changed",
            "categories",
            "internal_categories",
            "internal_categories_changed",
            "public_view_status",
            "first_published_on",
            "last_published_on",
            "unpublished_on",
            "latest_published_version",
            "unpublished_changes",
            "ready_to_be_published",
            "latest_note",
            "reported_on",
        )
        read_only_fields = (
            "id",
            "internal_code",
            "internal_id",
            "title_updated_on",
            "internal_title_changed",
            "internal_title_at_update",
            "summary_updated_on",
            "internal_summary_changed",
            "internal_summary_at_update",
            "status",
            "internal_status",
            "internal_status_changed",
            "status_date",
            "internal_status_date",
            "internal_status_date_changed",
            "is_resolved",
            "internal_is_resolved",
            "internal_is_resolved_changed",
            "country",
            "internal_country",
            "internal_country_changed",
            "trading_bloc",
            "internal_trading_bloc",
            "internal_trading_bloc_changed",
            "location",
            "internal_location",
            "internal_location_changed",
            "sectors",
            "internal_sectors",
            "internal_sectors_changed",
            "all_sectors",
            "internal_all_sectors",
            "internal_all_sectors_changed",
            "categories",
            "internal_categories",
            "internal_categories_changed",
            "public_view_status",
            "first_published_on",
            "last_published_on",
            "unpublished_on",
            "latest_published_version",
            "unpublished_changes",
            "ready_to_be_published",
            "latest_note",
            "reported_on",
        )

    def get_internal_title_changed(self, obj):
        return obj.internal_title_changed

    def get_internal_summary_changed(self, obj):
        return obj.internal_summary_changed

    def get_latest_published_version(self, obj):
        return PublishedVersionSerializer(obj.latest_published_version).data

    def get_unpublished_changes(self, obj):
        return obj.unpublished_changes

    def get_ready_to_be_published(self, obj):
        return obj.ready_to_be_published

    def get_internal_code(self, obj):
        return obj.barrier.code

    def get_internal_id(self, obj):
        return obj.barrier_id

    def get_latest_note(self, obj):
        try:
            note = obj.notes.latest("created_on")
            return PublicBarrierNoteSerializer(note).data
        except PublicBarrierNote.DoesNotExist:
            return None


class PublishedVersionSerializer(LocationFieldMixin,
                                 AllowNoneAtToRepresentationMixin,
                                 serializers.ModelSerializer):
    """
    Serializer to be used with DMAS FE app
    """
    id = serializers.CharField()
    title = serializers.CharField()
    summary = serializers.CharField()
    is_resolved = serializers.BooleanField()
    country = ReadOnlyCountryField()
    location = serializers.CharField()
    sectors = ReadOnlySectorsField()
    all_sectors = ReadOnlyAllSectorsField()
    categories = ReadOnlyCategoriesField()

    class Meta:
        model = PublicBarrier
        fields = (
            "id",
            "title",
            "summary",
            "is_resolved",
            "status_date",
            "country",
            "location",
            "sectors",
            "all_sectors",
            "categories",
        )


class PublicPublishedVersionSerializer(LocationFieldMixin,
                                       AllowNoneAtToRepresentationMixin,
                                       serializers.ModelSerializer):
    """
    Serializer to be used with gov.uk
    """
    id = HashidSerializerCharField(source_field=PUBLIC_ID, read_only=True)
    title = serializers.CharField()
    summary = serializers.CharField()
    country = ReadOnlyCountryField(to_repr_keys=("name", "trading_bloc"))
    trading_bloc = ReadOnlyTradingBlocField()
    sectors = serializers.SerializerMethodField()
    categories = ReadOnlyCategoriesField(to_repr_keys=("name",))
    reported_on = serializers.DateTimeField(source="internal_created_on")

    class Meta:
        model = PublicBarrier
        fields = (
            "id",
            "title",
            "summary",
            "is_resolved",
            "status_date",
            "country",
            # "caused_by_country_trading_bloc",
            "caused_by_trading_bloc",
            "trading_bloc",
            "location",
            "sectors",
            "categories",
            "last_published_on",
            "reported_on",
        )

    def get_sectors(self, obj):
        if obj.all_sectors:
            return [{"name": "All sectors"}]
        else:
            return ReadOnlySectorsField(to_repr_keys=("name",)).to_representation(obj.sectors)


def public_barriers_to_json(public_barriers=None):
    """
    Helper to serialize latest published version of published barriers.
    Public Barriers in the flat file should look similar.
    {
        "barriers": [
            {
                "id": "kjdfhkzx",
                "title": "Belgian chocolate...",
                "summary": "Lorem ipsum",
                "status": {"name": "Open: in progress",}
                "country": {"name": "Belgium",}
                "caused_by_trading_bloc": false,
                "trading_bloc": null,
                "location": "Belgium"
                "sectors: [
                    {"name": "Automotive"}
                ],
                "categories": [
                    {"name": "Goods and Services"}
                ],
                "last_published_on: "date",
                "reported_on": "date"
            }
        ]
    }
    If all sectors is true, use the sectors key to represent that as follows:
        "sectors: [{"name": "All sectors"}],
    """
    if public_barriers is None:
        public_barriers = (pb.latest_published_version for pb in get_published_public_barriers())
    serializer = PublicPublishedVersionSerializer(public_barriers, many=True)
    return serializer.data
