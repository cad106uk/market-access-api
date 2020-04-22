from django.urls import reverse
from freezegun import freeze_time
from rest_framework import status
from rest_framework.test import APITestCase

from api.barriers.models import BarrierInstance
from api.core.test_utils import APITestMixin, create_test_user
from api.interactions.models import Interaction
from tests.barriers.factories import ReportFactory, MinReportFactory


class TestSubmitReport(APITestMixin, APITestCase):

    def test_reported_as_resolved_in_full(self):
        resolved_in_full = 4
        report = ReportFactory(status=resolved_in_full, status_date="2020-02-02", status_summary="wibble")
        report.submit_report()

        barrier = BarrierInstance.objects.get(id=report.id)
        assert resolved_in_full == barrier.status

    def test_submit_report_records_user_as_reporter(self):
        expected_role = "Reporter"
        user = create_test_user(
            first_name="Marty", last_name="Bloggs", email="marty@wibble.com", username="marty.bloggs"
        )
        api_client = self.create_api_client(user=user)
        report = ReportFactory(created_by=user)
        members_url = reverse("list-members", kwargs={"pk": report.id})
        submit_url = reverse("submit-report", kwargs={"pk": report.id})

        response = api_client.get(members_url)
        assert status.HTTP_200_OK == response.status_code
        assert 0 == response.data["count"]

        response = api_client.put(submit_url)
        assert status.HTTP_200_OK == response.status_code

        response = api_client.get(members_url)
        assert status.HTTP_200_OK == response.status_code
        assert 1 == response.data["count"]
        member = response.data["results"][0]
        assert user.email == member["user"]["email"]
        assert user.first_name == member["user"]["first_name"]
        assert user.last_name == member["user"]["last_name"]
        assert expected_role == member["role"]

    def test_submit_report_without_all_sectors_and_sectors(self):
        report = ReportFactory(sectors=[], sectors_affected=True)
        assert not report.sectors

        url = reverse("submit-report", kwargs={"pk": report.id})
        submit_response = self.api_client.put(url, format="json", data={})

        assert submit_response.status_code == status.HTTP_400_BAD_REQUEST

    @freeze_time("2020-02-22")
    def test_submit_report_as_half_baked_user(self):
        user1 = create_test_user(
            first_name="", last_name="", email="billy@wibble.com", username=""
        )
        user2 = create_test_user(
            first_name="", last_name="", email="", username="WENDY@wobble.com"
        )
        user3 = create_test_user(
            first_name="", last_name="", email="", username="marty.bloggs"
        )
        user4 = create_test_user(
            first_name="", last_name="", email="Joe@wibble.com", username="joe.bloggs"
        )

        test_parameters = [
            {"user": user1, "expected_modified_user": "Billy"},
            {"user": user2, "expected_modified_user": "Wendy"},
            {"user": user3, "expected_modified_user": "Marty Bloggs"},
            {"user": user4, "expected_modified_user": "Joe Bloggs"},
        ]

        for tp in test_parameters:
            with self.subTest(tp=tp):
                report = ReportFactory()
                url = reverse("submit-report", kwargs={"pk": report.id})

                self.client.force_authenticate(user=tp["user"])
                submit_response = self.client.put(url, format="json", data={})

                assert submit_response.status_code == status.HTTP_200_OK
                report.refresh_from_db()
                assert not report.draft
                assert tp["user"] == report.modified_by
                assert tp["user"].id == report.modified_by_id
                assert "2020-02-22" == report.modified_on.strftime("%Y-%m-%d")
                assert tp["expected_modified_user"] == report.modified_user

    def test_submit_report_creates_an_interaction(self):
        report = ReportFactory()

        assert not Interaction.objects.filter(barrier=report)

        submit_url = reverse("submit-report", kwargs={"pk": report.id})
        response = self.api_client.put(submit_url)
        assert status.HTTP_200_OK == response.status_code

        assert 1 == Interaction.objects.filter(barrier=report).count()

    def test_no_interaction_is_created_when_submit_report_fails(self):
        report = ReportFactory(problem_status=None)

        assert not Interaction.objects.filter(barrier=report)

        submit_url = reverse("submit-report", kwargs={"pk": report.id})
        response = self.api_client.put(submit_url)
        assert status.HTTP_400_BAD_REQUEST == response.status_code

        assert not Interaction.objects.filter(barrier=report)

    @freeze_time("2020-02-02")
    def test_check_all_fields_after_report_submit_1(self):
        report = MinReportFactory(**{
            "problem_status": 2,
            "status": 2,
            "export_country": "66b795e0-ad71-4a65-9fa6-9f1e97e86d67",
            "trade_direction": 1,
            "sectors_affected": False,
            "product": "Some product",
            "source": "GOVT",
            "barrier_title": "Some title",
            "summary": "Some summary",
        })
        report.submit_report()

        url = reverse("get-barrier", kwargs={"pk": report.id})
        response = self.api_client.get(url)

        assert response.status_code == status.HTTP_200_OK
        assert response.data["id"]
        assert response.data["code"]
        assert response.data["reported_on"]
        assert 2 == response.data["problem_status"]
        assert "2020-02-02" == response.data["status_date"]
        assert "Some title" == response.data["barrier_title"]
        assert False == response.data["sectors_affected"]
        assert [] == response.data["sectors"]
        assert "66b795e0-ad71-4a65-9fa6-9f1e97e86d67" == response.data["export_country"]
        assert response.data["status"]["id"] == 2
        assert response.data["status"]["date"]
        assert not response.data["status"]["summary"]
        assert "UNKNOWN" == response.data["priority"]["code"]
        assert 0 == len(response.data["categories"])
        assert response.data["created_on"]

    def test_check_all_fields_after_report_submit_2(self):
        report = MinReportFactory(**{
            "problem_status": 2,
            "status_date": "2020-02-02",
            "status": 2,
            "status_summary": "some status summary",
            "export_country": "66b795e0-ad71-4a65-9fa6-9f1e97e86d67",
            "trade_direction": 2,
            "sectors_affected": True,
            "sectors": [
                "af959812-6095-e211-a939-e4115bead28a",
            ],
            "product": "Some product",
            "source": "GOVT",
            "barrier_title": "Some title",
            "summary": "Some summary",
        })
        report.submit_report()

        url = reverse("get-barrier", kwargs={"pk": report.id})
        response = self.api_client.get(url)

        assert response.status_code == status.HTTP_200_OK
        assert response.data["id"]
        assert response.data["code"]
        assert response.data["reported_on"]
        assert 2 == response.data["problem_status"]
        assert "2020-02-02" == response.data["status_date"]
        assert "Some title" == response.data["barrier_title"]
        assert True == response.data["sectors_affected"]
        assert ["af959812-6095-e211-a939-e4115bead28a"] == response.data["sectors"]
        assert "66b795e0-ad71-4a65-9fa6-9f1e97e86d67" == response.data["export_country"]
        assert response.data["status"]["id"] == 2
        assert response.data["status"]["date"]
        assert "some status summary" == response.data["status"]["summary"]
        assert "UNKNOWN" == response.data["priority"]["code"]
        assert 0 == len(response.data["categories"])
        assert response.data["created_on"]