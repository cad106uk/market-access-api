from django.test import TestCase
from rest_framework import status
from rest_framework.reverse import reverse

from freezegun import freeze_time
from rest_framework.test import APITestCase

from api.barriers.helpers import get_team_members
from api.barriers.models import Barrier
from api.metadata.models import Category, BarrierPriority, Organisation
from api.core.test_utils import APITestMixin
from tests.barriers.factories import BarrierFactory
from tests.metadata.factories import OrganisationFactory


class TestBarrierDetails(APITestMixin, APITestCase):

    def setUp(self):
        self.barrier = BarrierFactory()
        self.url = reverse("get-barrier", kwargs={"pk": self.barrier.id})

    def test_get_barrier_details(self):
        response = self.api_client.get(self.url)

        assert status.HTTP_200_OK == response.status_code
        assert str(self.barrier.id) == response.data["id"]

    def test_barrier_detail_by_code(self):
        url = reverse("barrier_detail_code", kwargs={"code": self.barrier.code})
        response = self.api_client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert str(self.barrier.id) == response.data["id"]

    def test_patch_barrier_status_to_resolved_in_full(self):
        assert 1 == self.barrier.status
        status_date = "2018-09-10"
        status_summary = "some status summary"
        resolved_in_full = 4

        url = reverse("resolve-in-full", kwargs={"pk": self.barrier.id})
        payload = {
            "status_date": status_date,
            "status_summary": status_summary,
        }
        response = self.api_client.put(url, format="json", data=payload)

        assert status.HTTP_200_OK == response.status_code
        self.barrier.refresh_from_db()
        assert resolved_in_full == self.barrier.status
        assert status_date == self.barrier.status_date.strftime('%Y-%m-%d')
        assert status_summary == self.barrier.status_summary

    @freeze_time("2020-02-22")
    def test_unknown_barrier_endpoint_sets_status_to_unknown(self):
        assert 1 == self.barrier.status
        status_summary = "some status summary"
        unknown = 7

        url = reverse("unknown-barrier", kwargs={"pk": self.barrier.id})
        payload = {
            "status_summary": status_summary,
        }
        response = self.api_client.put(url, format="json", data=payload)

        assert status.HTTP_200_OK == response.status_code
        self.barrier.refresh_from_db()
        assert unknown == self.barrier.status
        assert "2020-02-22" == self.barrier.status_date.strftime('%Y-%m-%d')
        assert status_summary == self.barrier.status_summary

    @freeze_time("2020-02-22")
    def test_open_in_progress_endpoint_sets_status_to_open_in_progress(self):
        assert 1 == self.barrier.status
        status_summary = "some status summary"
        open_in_progress = 2

        url = reverse("open-in-progress", kwargs={"pk": self.barrier.id})
        payload = {
            "status_summary": status_summary,
        }
        response = self.api_client.put(url, format="json", data=payload)

        assert status.HTTP_200_OK == response.status_code
        self.barrier.refresh_from_db()
        assert open_in_progress == self.barrier.status
        assert "2020-02-22" == self.barrier.status_date.strftime('%Y-%m-%d')
        assert status_summary == self.barrier.status_summary

    def test_patch_title(self):
        title = "Just a new title"
        payload = {
            "title": title
        }
        response = self.api_client.patch(self.url, format="json", data=payload)

        assert status.HTTP_200_OK == response.status_code
        assert str(self.barrier.id) == response.data["id"]
        assert title == response.data["title"]

    def test_patch_barrier_country(self):
        payload = {"country": "82756b9a-5d95-e211-a939-e4115bead28a"}
        response = self.api_client.patch(self.url, format="json", data=payload)

        assert status.HTTP_200_OK == response.status_code
        assert str(self.barrier.id) == response.data["id"]
        assert "82756b9a-5d95-e211-a939-e4115bead28a" == response.data["country"]["id"]

    def test_patch_barrier_trading_bloc(self):
        payload = {"trading_bloc": "TB00016"}
        response = self.api_client.patch(self.url, format="json", data=payload)

        assert status.HTTP_200_OK == response.status_code
        assert str(self.barrier.id) == response.data["id"]
        assert "TB00016" == response.data["trading_bloc"]["code"]

    def test_patch_barrier_caused_by_trading_bloc(self):
        payload = {
            "country": "82756b9a-5d95-e211-a939-e4115bead28a",
            "caused_by_trading_bloc": True,
        }
        response = self.api_client.patch(self.url, format="json", data=payload)

        assert status.HTTP_200_OK == response.status_code
        assert str(self.barrier.id) == response.data["id"]
        assert response.data["caused_by_trading_bloc"] is True

    def test_patch_barrier_term(self):
        assert 1 == self.barrier.term

        test_parameters = [
            {"term": None, "status_code": status.HTTP_200_OK, "expected_term": None},
            {"term": 2, "status_code": status.HTTP_200_OK, "expected_term": 2},
            {"term": 1, "status_code": status.HTTP_200_OK, "expected_term": 1},
            {"term": 0, "status_code": status.HTTP_400_BAD_REQUEST, "expected_term": 1},
            {"term": "ahoy!", "status_code": status.HTTP_400_BAD_REQUEST, "expected_term": 1},
            {"term": "987", "status_code": status.HTTP_400_BAD_REQUEST, "expected_term": 1},
        ]

        for tp in test_parameters:
            with self.subTest(tp=tp):
                payload = {"term": tp["term"],}
                response = self.api_client.patch(self.url, format="json", data=payload)

                self.barrier.refresh_from_db()
                assert tp["status_code"] == response.status_code, f"Test params: {tp}"
                assert tp["expected_term"] == self.barrier.term, f"Test params: {tp}"

    def test_patch_barrier_to_affect_all_sectors(self):
        assert not self.barrier.all_sectors
        assert 1 == len(self.barrier.sectors)

        payload = {"all_sectors": True}
        response = self.api_client.patch(self.url, format="json", data=payload)

        assert status.HTTP_200_OK == response.status_code
        assert str(self.barrier.id) == response.data["id"]
        assert response.data["all_sectors"] is True
        assert self.barrier.sectors == [sector["id"] for sector in response.data["sectors"]]

    def test_patch_barrier_priority(self):
        unknown_priority = BarrierPriority.objects.get(code="UNKNOWN")
        assert unknown_priority == self.barrier.priority

        priorities = ["HIGH", "MEDIUM", "LOW", "UNKNOWN"]

        for priority in priorities:
            with self.subTest(priority=priority):
                payload = {
                    "priority": priority,
                    "priority_summary": "wibble wobble"
                }

                response = self.api_client.patch(self.url, format="json", data=payload)

                assert status.HTTP_200_OK == response.status_code
                assert str(self.barrier.id) == response.data["id"]
                assert priority == response.data["priority"]["code"]

    def test_add_barrier_categories(self):
        categories = Category.objects.all()
        category1 = categories[0]
        category2 = categories[1]
        self.barrier.categories.add(category1)

        self.barrier.refresh_from_db()
        assert 1 == self.barrier.categories.count()

        payload = {
            "categories": (category1.id, category2.id)
        }
        response = self.api_client.patch(self.url, format="json", data=payload)

        assert status.HTTP_200_OK == response.status_code
        assert {category1.id, category2.id} == set([
            category["id"] for category in response.data["categories"]
        ])

    def test_replace_barrier_categories(self):
        categories = Category.objects.all()
        category1 = categories[0]
        category2 = categories[1]
        category3 = categories[2]
        self.barrier.categories.add(category1)

        self.barrier.refresh_from_db()
        assert 1 == self.barrier.categories.count()

        payload = {
            "categories": (category2.id, category3.id)
        }
        response = self.api_client.patch(self.url, format="json", data=payload)

        assert status.HTTP_200_OK == response.status_code
        assert {category2.id, category3.id} == set([
            category["id"] for category in response.data["categories"]
        ])

    def test_flush_barrier_categories(self):
        categories = Category.objects.all()
        category1 = categories[0]
        self.barrier.categories.add(category1)

        self.barrier.refresh_from_db()
        assert 1 == self.barrier.categories.count()

        payload = {
            "categories": ()
        }
        response = self.api_client.patch(self.url, format="json", data=payload)

        assert status.HTTP_200_OK == response.status_code
        assert not response.data["categories"]

    def test_update_barrier_adds_user_as_contributor(self):
        """ Users who edit a barrier should be  added as a Contributor automatically. """
        assert not get_team_members(self.barrier)

        payload = {"title": "Wibble wobble"}
        response = self.api_client.patch(self.url, format="json", data=payload)

        assert status.HTTP_200_OK == response.status_code
        team_members = get_team_members(self.barrier)
        assert 1 == team_members.count()
        assert "Contributor" == team_members.first().role

    def test_add_barrier_government_organisations(self):
        assert 0 == self.barrier.organisations.count()

        payload = {
            "government_organisations": ("1", "2")
        }
        response = self.api_client.patch(self.url, format="json", data=payload)

        assert status.HTTP_200_OK == response.status_code
        assert 2 == len(response.data["government_organisations"])
        assert {1, 2} == set([
            org.id for org in self.barrier.government_organisations
        ])

    def test_replace_barrier_government_organisations(self):
        org1 = Organisation.objects.get(id=1)
        org2 = Organisation.objects.get(id=2)
        org3 = Organisation.objects.get(id=3)
        self.barrier.organisations.add(org1, org2)

        assert 2 == self.barrier.government_organisations.count()

        payload = {
            "government_organisations": ("3",)
        }
        response = self.api_client.patch(self.url, format="json", data=payload)

        assert status.HTTP_200_OK == response.status_code
        assert 1 == len(response.data["government_organisations"])
        assert org3.id == response.data["government_organisations"][0]["id"]
        assert 1 == self.barrier.government_organisations.count()
        assert org3 == self.barrier.government_organisations.first()

    def test_flush_barrier_government_organisations(self):
        org1 = Organisation.objects.get(id=1)
        self.barrier.organisations.add(org1)

        self.barrier.refresh_from_db()
        assert 1 == self.barrier.government_organisations.count()

        payload = {
            "government_organisations": ()
        }
        response = self.api_client.patch(self.url, format="json", data=payload)

        assert status.HTTP_200_OK == response.status_code
        assert not response.data["government_organisations"]
        assert 0 == self.barrier.government_organisations.count()

    def test_flushing_government_organisations_leaves_other_organisations_intact(self):
        org1 = OrganisationFactory(name="Wibble", organisation_type=0)
        org2 = Organisation.objects.get(id=1)
        self.barrier.organisations.add(org1, org2)

        self.barrier.refresh_from_db()
        assert 2 == self.barrier.organisations.count()
        assert 1 == self.barrier.government_organisations.count()

        payload = {
            "government_organisations": ()
        }
        response = self.api_client.patch(self.url, format="json", data=payload)

        assert status.HTTP_200_OK == response.status_code
        assert not response.data["government_organisations"]
        assert 0 == self.barrier.government_organisations.count()
        assert 1 == self.barrier.organisations.count()
        assert org1 == self.barrier.organisations.first()


class TestHibernateEndpoint(APITestMixin, TestCase):

    def setUp(self):
        self.barrier = BarrierFactory()
        self.url = reverse("hibernate-barrier", kwargs={"pk": self.barrier.id})

    @freeze_time("2020-02-22")
    def test_hibernate_barrier_endpoint_sets_status_to_dormant(self):
        """
        Barrier status should be set to DORMANT when it gets hibernated.
        Also status date should be updated.
        """
        expected_status_date = "2020-02-22"
        dormant = 5
        assert 1 == self.barrier.status

        response = self.api_client.put(self.url)

        assert status.HTTP_200_OK == response.status_code
        self.barrier.refresh_from_db()
        assert dormant == self.barrier.status
        assert expected_status_date == self.barrier.status_date.strftime('%Y-%m-%d')

    def test_update_barrier_through_hibernate_barrier_endpoint(self):
        """
        Users should be able to update status summary while hibernating a barrier.
        """
        status_summary = "some status summary"

        payload = {"status_summary": status_summary}
        response = self.api_client.put(self.url, format="json", data=payload)

        assert status.HTTP_200_OK == response.status_code
        self.barrier.refresh_from_db()
        assert status_summary == self.barrier.status_summary


class TestBarrierTradeDirection(APITestMixin, TestCase):

    def setUp(self):
        self.barrier = BarrierFactory()
        self.url = reverse("get-barrier", kwargs={"pk": self.barrier.id})

    def test_get_barrier_without_trade_direction(self):
        """
        By default all existing barriers start with trade_direction not begin set.
        """
        self.barrier.trade_direction = None
        self.barrier.save()

        assert 1 == Barrier.objects.count()
        assert self.barrier.trade_direction is None

        response = self.api_client.get(self.url)

        assert status.HTTP_200_OK == response.status_code
        assert response.data["trade_direction"] is None

    def test_get_barrier_with_trade_direction(self):
        response = self.api_client.get(self.url)

        assert status.HTTP_200_OK == response.status_code
        assert 1 == response.data["trade_direction"]["id"]

    def test_set_trade_direction_to_none(self):
        """
        Trade direction cannot be set to None.
        """
        payload = {"trade_direction": None}
        response = self.api_client.patch(self.url, format="json", data=payload)

        assert status.HTTP_400_BAD_REQUEST == response.status_code
        assert 1 == self.barrier.trade_direction

    def test_patch_trade_direction(self):
        payload = {"trade_direction": 2}
        response = self.api_client.patch(self.url, format="json", data=payload)

        assert status.HTTP_200_OK == response.status_code
        assert 2 == response.data["trade_direction"]["id"]

    def test_patch_trade_direction_with_invalid_values(self):
        invalid_values = [0, 14, "123", "Wibble", [], {"a": 6}, "null"]

        for value in invalid_values:
            with self.subTest(value=value):
                payload = {"trade_direction": value}
                response = self.api_client.patch(self.url, format="json", data=payload)

                assert status.HTTP_400_BAD_REQUEST == response.status_code, \
                    f"Expected 400 when value is {value}"


class TestBarrierPublicEligibility(APITestMixin, TestCase):
    def setUp(self):
        self.barrier = BarrierFactory()
        self.url = reverse("get-barrier", kwargs={"pk": self.barrier.id})

    def test_get_barrier_without_public_eligibility(self):
        """
        By default all existing barriers start with public_eligibility not begin set.
        """

        assert 1 == Barrier.objects.count()
        assert self.barrier.public_eligibility is None

        response = self.api_client.get(self.url)

        assert status.HTTP_200_OK == response.status_code
        assert response.data["public_eligibility"] is None

    def test_patch_public_eligibility_with_valid_values(self):
        valid_values = [True, False]

        for value in valid_values:
            with self.subTest(value=value):
                payload = {"public_eligibility": value}
                response = self.api_client.patch(self.url, format="json", data=payload)

                assert status.HTTP_200_OK == response.status_code, \
                    f"Expected 200 when value is {value}"
                assert value == response.data["public_eligibility"], \
                    f'Expected {value} in "public_eligibility" field.'

    def test_patch_public_eligibility_with_invalid_values(self):
        invalid_values = [None, "", 123, {"1": "test"}, [1, 2, 3]]

        for value in invalid_values:
            with self.subTest(value=value):
                payload = {"public_eligibility": value}
                response = self.api_client.patch(self.url, format="json", data=payload)

                assert status.HTTP_400_BAD_REQUEST == response.status_code, \
                    f"Expected 400 when value is {value}"

    def test_patch_public_eligibility_summary(self):
        summary = "Wibble wobble"
        payload = {"public_eligibility_summary": summary}
        response = self.api_client.patch(self.url, format="json", data=payload)

        assert status.HTTP_200_OK == response.status_code, \
            f"Expected 200 when public_eligibility_summary is {summary}"
        assert summary == response.data["public_eligibility_summary"]

    def test_patch_public_eligibility_resets_public_eligibility_summary(self):
        self.barrier.public_eligibility = False
        self.barrier.public_eligibility_summary = "Wibble wobble"
        self.barrier.save()

        self.barrier.refresh_from_db()

        assert not self.barrier.public_eligibility
        assert self.barrier.public_eligibility_summary

        payload = {"public_eligibility": True}
        response = self.api_client.patch(self.url, format="json", data=payload)

        assert status.HTTP_200_OK == response.status_code
        assert response.data["public_eligibility"]
        assert not response.data["public_eligibility_summary"]

    def test_patch_public_eligibility_with_permissions(self):
        pass

    def test_patch_public_eligibility_without_permissions(self):
        pass
