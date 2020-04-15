from rest_framework import status
from rest_framework.reverse import reverse

from api.barriers.models import BarrierInstance
from api.core.test_utils import APITestMixin, create_test_user


class TestReportDetail(APITestMixin):
    def test_report_flow_stage_1(self):
        BarrierInstance(problem_status=1).save()
        instance = BarrierInstance.objects.first()
        url = reverse("get-report", kwargs={"pk": instance.id})
        response = self.api_client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert not response.data["progress"]

    def test_submit_stage_1_in_progress_1(self):
        url = reverse("list-reports")
        response = self.api_client.post(url, format="json", data={"problem_status": 1})

        assert response.status_code == status.HTTP_201_CREATED
        instance = BarrierInstance.objects.first()
        assert response.data["id"] == str(instance.id)

        detail_url = reverse("get-report", kwargs={"pk": instance.id})
        detail_response = self.api_client.get(detail_url)
        assert detail_response.status_code == status.HTTP_200_OK
        assert detail_response.data["problem_status"] == 1
        assert detail_response.data["status"] == 0
        assert detail_response.data["progress"]
        stage_1 = [
            d for d in detail_response.data["progress"] if d["stage_code"] == "1.1"
        ]
        assert stage_1[0]["status_desc"] == "IN PROGRESS"
        stage_2 = [
            d for d in detail_response.data["progress"] if d["stage_code"] == "1.2"
        ]
        assert stage_2[0]["status_desc"] == "NOT STARTED"
        stage_3 = [
            d for d in detail_response.data["progress"] if d["stage_code"] == "1.3"
        ]
        assert stage_3[0]["status_desc"] == "NOT STARTED"
        stage_4 = [
            d for d in detail_response.data["progress"] if d["stage_code"] == "1.4"
        ]
        assert stage_4[0]["status_desc"] == "NOT STARTED"

        submit_url = reverse("submit-report", kwargs={"pk": instance.id})
        submit_response = self.api_client.put(submit_url, format="json", data={})
        assert submit_response.status_code == status.HTTP_400_BAD_REQUEST

    def test_submit_stage_1_in_progress_2(self):
        url = reverse("list-reports")
        response = self.api_client.post(url, format="json", data={"problem_status": 2})

        assert response.status_code == status.HTTP_201_CREATED
        instance = BarrierInstance.objects.first()
        assert response.data["id"] == str(instance.id)

        detail_url = reverse("get-report", kwargs={"pk": instance.id})
        detail_response = self.api_client.get(detail_url)
        assert detail_response.status_code == status.HTTP_200_OK
        assert detail_response.data["problem_status"] == 2
        assert detail_response.data["status"] == 0
        assert detail_response.data["progress"]
        stage_1 = [
            d for d in detail_response.data["progress"] if d["stage_code"] == "1.1"
        ]
        assert stage_1[0]["status_desc"] == "IN PROGRESS"
        stage_2 = [
            d for d in detail_response.data["progress"] if d["stage_code"] == "1.2"
        ]
        assert stage_2[0]["status_desc"] == "NOT STARTED"
        stage_3 = [
            d for d in detail_response.data["progress"] if d["stage_code"] == "1.3"
        ]
        assert stage_3[0]["status_desc"] == "NOT STARTED"
        stage_4 = [
            d for d in detail_response.data["progress"] if d["stage_code"] == "1.4"
        ]
        assert stage_4[0]["status_desc"] == "NOT STARTED"

        submit_url = reverse("submit-report", kwargs={"pk": instance.id})
        submit_response = self.api_client.put(submit_url, format="json", data={})
        assert submit_response.status_code == status.HTTP_400_BAD_REQUEST

    def test_submit_stage_1_in_progress_is_resolved_false(self):
        url = reverse("list-reports")
        response = self.api_client.post(url, format="json", data={"status": 1})

        assert response.status_code == status.HTTP_201_CREATED
        instance = BarrierInstance.objects.first()
        assert response.data["id"] == str(instance.id)

        detail_url = reverse("get-report", kwargs={"pk": instance.id})
        detail_response = self.api_client.get(detail_url)
        assert detail_response.status_code == status.HTTP_200_OK
        assert detail_response.data["problem_status"] is None
        assert detail_response.data["status"] == 1
        assert detail_response.data["progress"]
        stage_1 = [
            d for d in detail_response.data["progress"] if d["stage_code"] == "1.1"
        ]
        assert stage_1[0]["status_desc"] == "IN PROGRESS"
        stage_2 = [
            d for d in detail_response.data["progress"] if d["stage_code"] == "1.2"
        ]
        assert stage_2[0]["status_desc"] == "NOT STARTED"
        stage_3 = [
            d for d in detail_response.data["progress"] if d["stage_code"] == "1.3"
        ]
        assert stage_3[0]["status_desc"] == "NOT STARTED"
        stage_4 = [
            d for d in detail_response.data["progress"] if d["stage_code"] == "1.4"
        ]
        assert stage_4[0]["status_desc"] == "NOT STARTED"

        submit_url = reverse("submit-report", kwargs={"pk": instance.id})
        submit_response = self.api_client.put(submit_url, format="json", data={})
        assert submit_response.status_code == status.HTTP_400_BAD_REQUEST

    def test_submit_stage_1_in_progress_is_resolved_true(self):
        url = reverse("list-reports")
        response = self.api_client.post(url, format="json", data={"status": 4, "status_date": "2018-04-01"})

        assert response.status_code == status.HTTP_201_CREATED
        instance = BarrierInstance.objects.first()
        assert response.data["id"] == str(instance.id)

        detail_url = reverse("get-report", kwargs={"pk": instance.id})
        detail_response = self.api_client.get(detail_url)
        assert detail_response.status_code == status.HTTP_200_OK
        assert detail_response.data["problem_status"] is None
        assert detail_response.data["status"] == 4
        assert detail_response.data["progress"]
        stage_1 = [
            d for d in detail_response.data["progress"] if d["stage_code"] == "1.1"
        ]
        assert stage_1[0]["status_desc"] == "IN PROGRESS"
        stage_2 = [
            d for d in detail_response.data["progress"] if d["stage_code"] == "1.2"
        ]
        assert stage_2[0]["status_desc"] == "NOT STARTED"
        stage_3 = [
            d for d in detail_response.data["progress"] if d["stage_code"] == "1.3"
        ]
        assert stage_3[0]["status_desc"] == "NOT STARTED"
        stage_4 = [
            d for d in detail_response.data["progress"] if d["stage_code"] == "1.4"
        ]
        assert stage_4[0]["status_desc"] == "NOT STARTED"

        submit_url = reverse("submit-report", kwargs={"pk": instance.id})
        submit_response = self.api_client.put(submit_url, format="json", data={})
        assert submit_response.status_code == status.HTTP_400_BAD_REQUEST

    def test_list_reports_post_stage_1_in_progress_is_resolved_true_no_date(self):
        url = reverse("list-reports")
        response = self.api_client.post(
            url, format="json", data={"problem_status": 2, "status": 4}
        )

        assert response.status_code == status.HTTP_201_CREATED
        instance = BarrierInstance.objects.first()
        assert response.data["id"] == str(instance.id)

        detail_url = reverse("get-report", kwargs={"pk": instance.id})
        detail_response = self.api_client.get(detail_url)
        assert detail_response.status_code == status.HTTP_200_OK
        assert detail_response.data["problem_status"] == 2
        assert detail_response.data["status"] == 4
        assert detail_response.data["progress"]
        stage_1 = [
            d for d in detail_response.data["progress"] if d["stage_code"] == "1.1"
        ]
        assert stage_1[0]["status_desc"] == "IN PROGRESS"
        stage_2 = [
            d for d in detail_response.data["progress"] if d["stage_code"] == "1.2"
        ]
        assert stage_2[0]["status_desc"] == "NOT STARTED"
        stage_3 = [
            d for d in detail_response.data["progress"] if d["stage_code"] == "1.3"
        ]
        assert stage_3[0]["status_desc"] == "NOT STARTED"
        stage_4 = [
            d for d in detail_response.data["progress"] if d["stage_code"] == "1.4"
        ]
        assert stage_4[0]["status_desc"] == "NOT STARTED"

        submit_url = reverse("submit-report", kwargs={"pk": instance.id})
        submit_response = self.api_client.put(submit_url, format="json", data={})
        assert submit_response.status_code == status.HTTP_400_BAD_REQUEST

    def test_submit_stage_1_completed(self):
        url = reverse("list-reports")
        response = self.api_client.post(
            url, format="json", data={"problem_status": 2, "status": 1}
        )

        assert response.status_code == status.HTTP_201_CREATED
        instance = BarrierInstance.objects.first()
        assert response.data["id"] == str(instance.id)

        detail_url = reverse("get-report", kwargs={"pk": instance.id})
        detail_response = self.api_client.get(detail_url)
        assert detail_response.status_code == status.HTTP_200_OK
        assert detail_response.data["problem_status"] == 2
        assert detail_response.data["status"] == 1
        assert detail_response.data["progress"]
        stage_1 = [
            d for d in detail_response.data["progress"] if d["stage_code"] == "1.1"
        ]
        assert stage_1[0]["status_desc"] == "COMPLETED"
        stage_2 = [
            d for d in detail_response.data["progress"] if d["stage_code"] == "1.2"
        ]
        assert stage_2[0]["status_desc"] == "NOT STARTED"
        stage_3 = [
            d for d in detail_response.data["progress"] if d["stage_code"] == "1.3"
        ]
        assert stage_3[0]["status_desc"] == "NOT STARTED"
        stage_4 = [
            d for d in detail_response.data["progress"] if d["stage_code"] == "1.4"
        ]
        assert stage_4[0]["status_desc"] == "NOT STARTED"

        submit_url = reverse("submit-report", kwargs={"pk": instance.id})
        submit_response = self.api_client.put(submit_url, format="json", data={})
        assert submit_response.status_code == status.HTTP_400_BAD_REQUEST

    def test_submit_stage_2_completed(self):
        url = reverse("list-reports")
        response = self.api_client.post(
            url,
            format="json",
            data={"export_country": "66b795e0-ad71-4a65-9fa6-9f1e97e86d67"},
        )

        assert response.status_code == status.HTTP_201_CREATED
        instance = BarrierInstance.objects.first()
        assert response.data["id"] == str(instance.id)

        detail_url = reverse("get-report", kwargs={"pk": instance.id})
        detail_response = self.api_client.get(detail_url)
        assert detail_response.status_code == status.HTTP_200_OK
        assert detail_response.data["problem_status"] is None
        assert (
            detail_response.data["export_country"]
            == "66b795e0-ad71-4a65-9fa6-9f1e97e86d67"
        )
        assert detail_response.data["progress"]
        stage_1 = [
            d for d in detail_response.data["progress"] if d["stage_code"] == "1.1"
        ]
        assert stage_1[0]["status_desc"] == "NOT STARTED"
        stage_2 = [
            d for d in detail_response.data["progress"] if d["stage_code"] == "1.2"
        ]
        assert stage_2[0]["status_desc"] == "COMPLETED"
        stage_3 = [
            d for d in detail_response.data["progress"] if d["stage_code"] == "1.3"
        ]
        assert stage_3[0]["status_desc"] == "NOT STARTED"
        stage_4 = [
            d for d in detail_response.data["progress"] if d["stage_code"] == "1.4"
        ]
        assert stage_4[0]["status_desc"] == "NOT STARTED"

        submit_url = reverse("submit-report", kwargs={"pk": instance.id})
        submit_response = self.api_client.put(submit_url, format="json", data={})
        assert submit_response.status_code == status.HTTP_400_BAD_REQUEST

    def test_submit_stage_1_in_progress_and_2_completed(self):
        url = reverse("list-reports")
        response = self.api_client.post(
            url,
            format="json",
            data={
                "problem_status": 2,
                "export_country": "66b795e0-ad71-4a65-9fa6-9f1e97e86d67",
            },
        )

        assert response.status_code == status.HTTP_201_CREATED
        instance = BarrierInstance.objects.first()
        assert response.data["id"] == str(instance.id)

        detail_url = reverse("get-report", kwargs={"pk": instance.id})
        detail_response = self.api_client.get(detail_url)
        assert detail_response.status_code == status.HTTP_200_OK
        assert detail_response.data["problem_status"] == 2
        assert detail_response.data["status"] == 0
        assert (
            detail_response.data["export_country"]
            == "66b795e0-ad71-4a65-9fa6-9f1e97e86d67"
        )
        assert detail_response.data["progress"]
        stage_1 = [
            d for d in detail_response.data["progress"] if d["stage_code"] == "1.1"
        ]
        assert stage_1[0]["status_desc"] == "IN PROGRESS"
        stage_2 = [
            d for d in detail_response.data["progress"] if d["stage_code"] == "1.2"
        ]
        assert stage_2[0]["status_desc"] == "COMPLETED"
        stage_3 = [
            d for d in detail_response.data["progress"] if d["stage_code"] == "1.3"
        ]
        assert stage_3[0]["status_desc"] == "NOT STARTED"
        stage_4 = [
            d for d in detail_response.data["progress"] if d["stage_code"] == "1.4"
        ]
        assert stage_4[0]["status_desc"] == "NOT STARTED"

        submit_url = reverse("submit-report", kwargs={"pk": instance.id})
        submit_response = self.api_client.put(submit_url, format="json", data={})
        assert submit_response.status_code == status.HTTP_400_BAD_REQUEST

    def test_submit_stage_1_and_2_completed(self):
        url = reverse("list-reports")
        response = self.api_client.post(
            url,
            format="json",
            data={
                "problem_status": 2,
                "status": 1,
                "export_country": "66b795e0-ad71-4a65-9fa6-9f1e97e86d67",
            },
        )

        assert response.status_code == status.HTTP_201_CREATED
        instance = BarrierInstance.objects.first()
        assert response.data["id"] == str(instance.id)

        detail_url = reverse("get-report", kwargs={"pk": instance.id})
        detail_response = self.api_client.get(detail_url)
        assert detail_response.status_code == status.HTTP_200_OK
        assert detail_response.data["problem_status"] == 2
        assert detail_response.data["status"] == 1
        assert (
            detail_response.data["export_country"]
            == "66b795e0-ad71-4a65-9fa6-9f1e97e86d67"
        )
        assert detail_response.data["progress"]
        stage_1 = [
            d for d in detail_response.data["progress"] if d["stage_code"] == "1.1"
        ]
        assert stage_1[0]["status_desc"] == "COMPLETED"
        stage_2 = [
            d for d in detail_response.data["progress"] if d["stage_code"] == "1.2"
        ]
        assert stage_2[0]["status_desc"] == "COMPLETED"
        stage_3 = [
            d for d in detail_response.data["progress"] if d["stage_code"] == "1.3"
        ]
        assert stage_3[0]["status_desc"] == "NOT STARTED"
        stage_4 = [
            d for d in detail_response.data["progress"] if d["stage_code"] == "1.4"
        ]
        assert stage_4[0]["status_desc"] == "NOT STARTED"

        submit_url = reverse("submit-report", kwargs={"pk": instance.id})
        submit_response = self.api_client.put(submit_url, format="json", data={})
        assert submit_response.status_code == status.HTTP_400_BAD_REQUEST

    def test_submit_stage_3_in_progress(self):
        url = reverse("list-reports")
        response = self.api_client.post(
            url, format="json", data={"sectors_affected": True}
        )

        assert response.status_code == status.HTTP_201_CREATED
        instance = BarrierInstance.objects.first()
        assert response.data["id"] == str(instance.id)

        detail_url = reverse("get-report", kwargs={"pk": instance.id})
        detail_response = self.api_client.get(detail_url)
        assert detail_response.status_code == status.HTTP_200_OK
        assert detail_response.data["problem_status"] is None
        assert detail_response.data["sectors_affected"] is True
        assert detail_response.data["progress"]
        stage_1 = [
            d for d in detail_response.data["progress"] if d["stage_code"] == "1.1"
        ]
        assert stage_1[0]["status_desc"] == "NOT STARTED"
        stage_2 = [
            d for d in detail_response.data["progress"] if d["stage_code"] == "1.2"
        ]
        assert stage_2[0]["status_desc"] == "NOT STARTED"
        stage_3 = [
            d for d in detail_response.data["progress"] if d["stage_code"] == "1.3"
        ]
        assert stage_3[0]["status_desc"] == "COMPLETED"
        stage_4 = [
            d for d in detail_response.data["progress"] if d["stage_code"] == "1.4"
        ]
        assert stage_4[0]["status_desc"] == "NOT STARTED"

        submit_url = reverse("submit-report", kwargs={"pk": instance.id})
        submit_response = self.api_client.put(submit_url, format="json", data={})
        assert submit_response.status_code == status.HTTP_400_BAD_REQUEST

    def test_submit_stage_3_completed_option_1(self):
        url = reverse("list-reports")
        response = self.api_client.post(
            url, format="json", data={"sectors_affected": False}
        )

        assert response.status_code == status.HTTP_201_CREATED
        instance = BarrierInstance.objects.first()
        assert response.data["id"] == str(instance.id)

        detail_url = reverse("get-report", kwargs={"pk": instance.id})
        detail_response = self.api_client.get(detail_url)
        assert detail_response.status_code == status.HTTP_200_OK
        assert detail_response.data["problem_status"] is None
        assert detail_response.data["sectors_affected"] is False
        assert detail_response.data["progress"]
        stage_1 = [
            d for d in detail_response.data["progress"] if d["stage_code"] == "1.1"
        ]
        assert stage_1[0]["status_desc"] == "NOT STARTED"
        stage_2 = [
            d for d in detail_response.data["progress"] if d["stage_code"] == "1.2"
        ]
        assert stage_2[0]["status_desc"] == "NOT STARTED"
        stage_3 = [
            d for d in detail_response.data["progress"] if d["stage_code"] == "1.3"
        ]
        assert stage_3[0]["status_desc"] == "COMPLETED"
        stage_4 = [
            d for d in detail_response.data["progress"] if d["stage_code"] == "1.4"
        ]
        assert stage_4[0]["status_desc"] == "NOT STARTED"

        submit_url = reverse("submit-report", kwargs={"pk": instance.id})
        submit_response = self.api_client.put(submit_url, format="json", data={})
        assert submit_response.status_code == status.HTTP_400_BAD_REQUEST

    def test_submit_stage_3_completed_option_2(self):
        url = reverse("list-reports")
        response = self.api_client.post(
            url,
            format="json",
            data={
                "sectors_affected": True,
                "sectors": [
                    "af959812-6095-e211-a939-e4115bead28a",
                    "9538cecc-5f95-e211-a939-e4115bead28a",
                ],
            },
        )

        assert response.status_code == status.HTTP_201_CREATED
        instance = BarrierInstance.objects.first()
        assert response.data["id"] == str(instance.id)

        detail_url = reverse("get-report", kwargs={"pk": instance.id})
        detail_response = self.api_client.get(detail_url)
        assert detail_response.status_code == status.HTTP_200_OK
        assert detail_response.data["problem_status"] is None
        assert detail_response.data["sectors_affected"] is True
        assert detail_response.data["sectors"]
        assert detail_response.data["progress"]
        stage_1 = [
            d for d in detail_response.data["progress"] if d["stage_code"] == "1.1"
        ]
        assert stage_1[0]["status_desc"] == "NOT STARTED"
        stage_2 = [
            d for d in detail_response.data["progress"] if d["stage_code"] == "1.2"
        ]
        assert stage_2[0]["status_desc"] == "NOT STARTED"
        stage_3 = [
            d for d in detail_response.data["progress"] if d["stage_code"] == "1.3"
        ]
        assert stage_3[0]["status_desc"] == "COMPLETED"
        stage_4 = [
            d for d in detail_response.data["progress"] if d["stage_code"] == "1.4"
        ]
        assert stage_4[0]["status_desc"] == "NOT STARTED"

        submit_url = reverse("submit-report", kwargs={"pk": instance.id})
        submit_response = self.api_client.put(submit_url, format="json", data={})
        assert submit_response.status_code == status.HTTP_400_BAD_REQUEST

    def test_submit_stage_1_in_progress_2_completed_3_completed_1(self):
        pass

    def test_submit_stage_1_in_progress_2_completed_3_completed_2(self):
        pass

    def test_submit_stage_1_2_completed_3_completed_1(self):
        pass

    def test_submit_stage_1_2_completed_3_completed_2(self):
        pass

    def test_submit_stage_4_in_progress_product(self):
        url = reverse("list-reports")
        response = self.api_client.post(
            url, format="json", data={"product": "Some product"}
        )

        assert response.status_code == status.HTTP_201_CREATED
        instance = BarrierInstance.objects.first()
        assert response.data["id"] == str(instance.id)

        detail_url = reverse("get-report", kwargs={"pk": instance.id})
        detail_response = self.api_client.get(detail_url)
        assert detail_response.status_code == status.HTTP_200_OK
        assert detail_response.data["product"] == "Some product"
        assert detail_response.data["source"] is None
        assert detail_response.data["other_source"] is None
        assert detail_response.data["barrier_title"] is None
        assert detail_response.data["summary"] is None
        stage_1 = [
            d for d in detail_response.data["progress"] if d["stage_code"] == "1.1"
        ]
        assert stage_1[0]["status_desc"] == "NOT STARTED"
        stage_2 = [
            d for d in detail_response.data["progress"] if d["stage_code"] == "1.2"
        ]
        assert stage_2[0]["status_desc"] == "NOT STARTED"
        stage_3 = [
            d for d in detail_response.data["progress"] if d["stage_code"] == "1.3"
        ]
        assert stage_3[0]["status_desc"] == "NOT STARTED"
        stage_4 = [
            d for d in detail_response.data["progress"] if d["stage_code"] == "1.4"
        ]
        assert stage_4[0]["status_desc"] == "IN PROGRESS"

        submit_url = reverse("submit-report", kwargs={"pk": instance.id})
        submit_response = self.api_client.put(submit_url, format="json", data={})
        assert submit_response.status_code == status.HTTP_400_BAD_REQUEST

    def test_submit_stage_4_in_progress_source(self):
        url = reverse("list-reports")
        response = self.api_client.post(url, format="json", data={"source": "GOVT"})

        assert response.status_code == status.HTTP_201_CREATED
        instance = BarrierInstance.objects.first()
        assert response.data["id"] == str(instance.id)

        detail_url = reverse("get-report", kwargs={"pk": instance.id})
        detail_response = self.api_client.get(detail_url)
        assert detail_response.status_code == status.HTTP_200_OK
        assert detail_response.data["product"] is None
        assert detail_response.data["source"] == "GOVT"
        assert detail_response.data["other_source"] is None
        assert detail_response.data["barrier_title"] is None
        assert detail_response.data["summary"] is None
        stage_1 = [
            d for d in detail_response.data["progress"] if d["stage_code"] == "1.1"
        ]
        assert stage_1[0]["status_desc"] == "NOT STARTED"
        stage_2 = [
            d for d in detail_response.data["progress"] if d["stage_code"] == "1.2"
        ]
        assert stage_2[0]["status_desc"] == "NOT STARTED"
        stage_3 = [
            d for d in detail_response.data["progress"] if d["stage_code"] == "1.3"
        ]
        assert stage_3[0]["status_desc"] == "NOT STARTED"
        stage_4 = [
            d for d in detail_response.data["progress"] if d["stage_code"] == "1.4"
        ]
        assert stage_4[0]["status_desc"] == "IN PROGRESS"

        submit_url = reverse("submit-report", kwargs={"pk": instance.id})
        submit_response = self.api_client.put(submit_url, format="json", data={})
        assert submit_response.status_code == status.HTTP_400_BAD_REQUEST

    def test_submit_stage_4_in_progress_other_source(self):
        url = reverse("list-reports")
        response = self.api_client.post(url, format="json", data={"source": "OTHER"})

        assert response.status_code == status.HTTP_201_CREATED
        instance = BarrierInstance.objects.first()
        assert response.data["id"] == str(instance.id)

        detail_url = reverse("get-report", kwargs={"pk": instance.id})
        detail_response = self.api_client.get(detail_url)
        assert detail_response.status_code == status.HTTP_200_OK
        assert detail_response.data["product"] is None
        assert detail_response.data["source"] == "OTHER"
        assert detail_response.data["other_source"] is None
        assert detail_response.data["barrier_title"] is None
        assert detail_response.data["summary"] is None
        stage_1 = [
            d for d in detail_response.data["progress"] if d["stage_code"] == "1.1"
        ]
        assert stage_1[0]["status_desc"] == "NOT STARTED"
        stage_2 = [
            d for d in detail_response.data["progress"] if d["stage_code"] == "1.2"
        ]
        assert stage_2[0]["status_desc"] == "NOT STARTED"
        stage_3 = [
            d for d in detail_response.data["progress"] if d["stage_code"] == "1.3"
        ]
        assert stage_3[0]["status_desc"] == "NOT STARTED"
        stage_4 = [
            d for d in detail_response.data["progress"] if d["stage_code"] == "1.4"
        ]
        assert stage_4[0]["status_desc"] == "IN PROGRESS"

        submit_url = reverse("submit-report", kwargs={"pk": instance.id})
        submit_response = self.api_client.put(submit_url, format="json", data={})
        assert submit_response.status_code == status.HTTP_400_BAD_REQUEST

    def test_submit_stage_4_in_progress_barrier_title(self):
        url = reverse("list-reports")
        response = self.api_client.post(
            url, format="json", data={"barrier_title": "Some title"}
        )

        assert response.status_code == status.HTTP_201_CREATED
        instance = BarrierInstance.objects.first()
        assert response.data["id"] == str(instance.id)

        detail_url = reverse("get-report", kwargs={"pk": instance.id})
        detail_response = self.api_client.get(detail_url)
        assert detail_response.status_code == status.HTTP_200_OK
        assert detail_response.data["product"] is None
        assert detail_response.data["source"] is None
        assert detail_response.data["other_source"] is None
        assert detail_response.data["barrier_title"] == "Some title"
        assert detail_response.data["summary"] is None
        stage_1 = [
            d for d in detail_response.data["progress"] if d["stage_code"] == "1.1"
        ]
        assert stage_1[0]["status_desc"] == "NOT STARTED"
        stage_2 = [
            d for d in detail_response.data["progress"] if d["stage_code"] == "1.2"
        ]
        assert stage_2[0]["status_desc"] == "NOT STARTED"
        stage_3 = [
            d for d in detail_response.data["progress"] if d["stage_code"] == "1.3"
        ]
        assert stage_3[0]["status_desc"] == "NOT STARTED"
        stage_4 = [
            d for d in detail_response.data["progress"] if d["stage_code"] == "1.4"
        ]
        assert stage_4[0]["status_desc"] == "IN PROGRESS"

        submit_url = reverse("submit-report", kwargs={"pk": instance.id})
        submit_response = self.api_client.put(submit_url, format="json", data={})
        assert submit_response.status_code == status.HTTP_400_BAD_REQUEST

    def test_submit_stage_4_in_progress_summary(self):
        url = reverse("list-reports")
        response = self.api_client.post(
            url,
            format="json",
            data={
                "status": 4,
                "status_date": "2018-09-10",
                "summary": "Some summary",
            },
        )

        assert response.status_code == status.HTTP_201_CREATED
        instance = BarrierInstance.objects.first()
        assert response.data["id"] == str(instance.id)

        detail_url = reverse("get-report", kwargs={"pk": instance.id})
        detail_response = self.api_client.get(detail_url)
        assert detail_response.status_code == status.HTTP_200_OK
        assert detail_response.data["product"] is None
        assert detail_response.data["source"] is None
        assert detail_response.data["other_source"] is None
        assert detail_response.data["barrier_title"] is None
        assert detail_response.data["summary"] == "Some summary"
        stage_1 = [
            d for d in detail_response.data["progress"] if d["stage_code"] == "1.1"
        ]
        assert stage_1[0]["status_desc"] == "IN PROGRESS"
        stage_2 = [
            d for d in detail_response.data["progress"] if d["stage_code"] == "1.2"
        ]
        assert stage_2[0]["status_desc"] == "NOT STARTED"
        stage_3 = [
            d for d in detail_response.data["progress"] if d["stage_code"] == "1.3"
        ]
        assert stage_3[0]["status_desc"] == "NOT STARTED"
        stage_4 = [
            d for d in detail_response.data["progress"] if d["stage_code"] == "1.4"
        ]
        assert stage_4[0]["status_desc"] == "NOT STARTED"
        stage_5 = [
            d for d in detail_response.data["progress"] if d["stage_code"] == "1.5"
        ]
        assert stage_5[0]["status_desc"] == "COMPLETED"

        submit_url = reverse("submit-report", kwargs={"pk": instance.id})
        submit_response = self.api_client.put(submit_url, format="json", data={})
        assert submit_response.status_code == status.HTTP_400_BAD_REQUEST

    def test_submit_stage_4_not_completed(self):
        url = reverse("list-reports")
        response = self.api_client.post(
            url,
            format="json",
            data={
                "product": "Some product",
                "source": "OTHER",
                "barrier_title": "Some title",
                "summary": "Some summary",
            },
        )

        assert response.status_code == status.HTTP_201_CREATED
        instance = BarrierInstance.objects.first()
        assert response.data["id"] == str(instance.id)

        detail_url = reverse("get-report", kwargs={"pk": instance.id})
        detail_response = self.api_client.get(detail_url)
        assert detail_response.status_code == status.HTTP_200_OK
        assert detail_response.data["product"] == "Some product"
        assert detail_response.data["source"] == "OTHER"
        assert detail_response.data["other_source"] is None
        assert detail_response.data["barrier_title"] == "Some title"
        assert detail_response.data["summary"] == "Some summary"
        stage_1 = [
            d for d in detail_response.data["progress"] if d["stage_code"] == "1.1"
        ]
        assert stage_1[0]["status_desc"] == "NOT STARTED"
        stage_2 = [
            d for d in detail_response.data["progress"] if d["stage_code"] == "1.2"
        ]
        assert stage_2[0]["status_desc"] == "NOT STARTED"
        stage_3 = [
            d for d in detail_response.data["progress"] if d["stage_code"] == "1.3"
        ]
        assert stage_3[0]["status_desc"] == "NOT STARTED"
        stage_4 = [
            d for d in detail_response.data["progress"] if d["stage_code"] == "1.4"
        ]
        assert stage_4[0]["status_desc"] == "IN PROGRESS"

        submit_url = reverse("submit-report", kwargs={"pk": instance.id})
        submit_response = self.api_client.put(submit_url, format="json", data={})
        assert submit_response.status_code == status.HTTP_400_BAD_REQUEST

    def test_submit_stage_4_completed_2(self):
        url = reverse("list-reports")
        response = self.api_client.post(
            url,
            format="json",
            data={
                "product": "Some product",
                "source": "OTHER",
                "other_source": "Not sure",
                "barrier_title": "Some title",
                "summary": "Some summary",
            },
        )

        assert response.status_code == status.HTTP_201_CREATED
        instance = BarrierInstance.objects.first()
        assert response.data["id"] == str(instance.id)

        detail_url = reverse("get-report", kwargs={"pk": instance.id})
        detail_response = self.api_client.get(detail_url)
        assert detail_response.status_code == status.HTTP_200_OK
        assert detail_response.data["product"] == "Some product"
        assert detail_response.data["source"] == "OTHER"
        assert detail_response.data["other_source"] == "Not sure"
        assert detail_response.data["barrier_title"] == "Some title"
        assert detail_response.data["summary"] == "Some summary"
        stage_1 = [
            d for d in detail_response.data["progress"] if d["stage_code"] == "1.1"
        ]
        assert stage_1[0]["status_desc"] == "NOT STARTED"
        stage_2 = [
            d for d in detail_response.data["progress"] if d["stage_code"] == "1.2"
        ]
        assert stage_2[0]["status_desc"] == "NOT STARTED"
        stage_3 = [
            d for d in detail_response.data["progress"] if d["stage_code"] == "1.3"
        ]
        assert stage_3[0]["status_desc"] == "NOT STARTED"
        stage_4 = [
            d for d in detail_response.data["progress"] if d["stage_code"] == "1.4"
        ]
        assert stage_4[0]["status_desc"] == "COMPLETED"

        submit_url = reverse("submit-report", kwargs={"pk": instance.id})
        submit_response = self.api_client.put(submit_url, format="json", data={})
        assert submit_response.status_code == status.HTTP_400_BAD_REQUEST

    def test_submit_stage_4_completed(self):
        url = reverse("list-reports")
        response = self.api_client.post(
            url,
            format="json",
            data={
                "product": "Some product",
                "source": "GOVT",
                "barrier_title": "Some title",
                "summary": "Some summary",
            },
        )

        assert response.status_code == status.HTTP_201_CREATED
        instance = BarrierInstance.objects.first()
        assert response.data["id"] == str(instance.id)

        detail_url = reverse("get-report", kwargs={"pk": instance.id})
        detail_response = self.api_client.get(detail_url)
        assert detail_response.status_code == status.HTTP_200_OK
        assert detail_response.data["product"] == "Some product"
        assert detail_response.data["source"] == "GOVT"
        assert detail_response.data["barrier_title"] == "Some title"
        assert detail_response.data["summary"] == "Some summary"
        stage_1 = [
            d for d in detail_response.data["progress"] if d["stage_code"] == "1.1"
        ]
        assert stage_1[0]["status_desc"] == "NOT STARTED"
        stage_2 = [
            d for d in detail_response.data["progress"] if d["stage_code"] == "1.2"
        ]
        assert stage_2[0]["status_desc"] == "NOT STARTED"
        stage_3 = [
            d for d in detail_response.data["progress"] if d["stage_code"] == "1.3"
        ]
        assert stage_3[0]["status_desc"] == "NOT STARTED"
        stage_4 = [
            d for d in detail_response.data["progress"] if d["stage_code"] == "1.4"
        ]
        assert stage_4[0]["status_desc"] == "COMPLETED"

        submit_url = reverse("submit-report", kwargs={"pk": instance.id})
        submit_response = self.api_client.put(submit_url, format="json", data={})
        assert submit_response.status_code == status.HTTP_400_BAD_REQUEST

    def test_submit_completed_report_1(self):
        url = reverse("list-reports")
        response = self.api_client.post(
            url,
            format="json",
            data={
                "problem_status": 2,
                "status": 1,
                "export_country": "66b795e0-ad71-4a65-9fa6-9f1e97e86d67",
                "sectors_affected": True,
                "sectors": [
                    "af959812-6095-e211-a939-e4115bead28a",
                    "9538cecc-5f95-e211-a939-e4115bead28a",
                ],
                "product": "Some product",
                "source": "GOVT",
                "barrier_title": "Some title",
                "summary": "Some summary",
            },
        )

        assert response.status_code == status.HTTP_201_CREATED
        instance = BarrierInstance.objects.first()
        assert response.data["id"] == str(instance.id)

        detail_url = reverse("get-report", kwargs={"pk": instance.id})
        detail_response = self.api_client.get(detail_url)
        assert detail_response.status_code == status.HTTP_200_OK
        assert detail_response.data["problem_status"] == 2
        assert detail_response.data["status"] == 1
        assert (
            detail_response.data["export_country"]
            == "66b795e0-ad71-4a65-9fa6-9f1e97e86d67"
        )
        assert detail_response.data["sectors_affected"] is True
        assert detail_response.data["sectors"] == [
            "af959812-6095-e211-a939-e4115bead28a",
            "9538cecc-5f95-e211-a939-e4115bead28a",
        ]
        assert detail_response.data["product"] == "Some product"
        assert detail_response.data["source"] == "GOVT"
        assert detail_response.data["barrier_title"] == "Some title"
        assert detail_response.data["summary"] == "Some summary"
        stage_1 = [
            d for d in detail_response.data["progress"] if d["stage_code"] == "1.1"
        ]
        assert stage_1[0]["status_desc"] == "COMPLETED"
        stage_2 = [
            d for d in detail_response.data["progress"] if d["stage_code"] == "1.2"
        ]
        assert stage_2[0]["status_desc"] == "COMPLETED"
        stage_3 = [
            d for d in detail_response.data["progress"] if d["stage_code"] == "1.3"
        ]
        assert stage_3[0]["status_desc"] == "COMPLETED"
        stage_4 = [
            d for d in detail_response.data["progress"] if d["stage_code"] == "1.4"
        ]
        assert stage_4[0]["status_desc"] == "COMPLETED"

        submit_url = reverse("submit-report", kwargs={"pk": instance.id})
        submit_response = self.api_client.put(submit_url, format="json", data={})
        assert submit_response.status_code == status.HTTP_200_OK

    def test_submit_completed_report_2(self):
        url = reverse("list-reports")
        response = self.api_client.post(
            url,
            format="json",
            data={
                "problem_status": 2,
                "status": 1,
                "export_country": "66b795e0-ad71-4a65-9fa6-9f1e97e86d67",
                "sectors_affected": True,
                "sectors": [
                    "af959812-6095-e211-a939-e4115bead28a",
                    "9538cecc-5f95-e211-a939-e4115bead28a",
                ],
                "product": "Some product",
                "source": "OTHER",
                "other_source": "Other source",
                "barrier_title": "Some title",
                "summary": "Some summary",
            },
        )

        assert response.status_code == status.HTTP_201_CREATED
        instance = BarrierInstance.objects.first()
        assert response.data["id"] == str(instance.id)

        detail_url = reverse("get-report", kwargs={"pk": instance.id})
        detail_response = self.api_client.get(detail_url)
        assert detail_response.status_code == status.HTTP_200_OK
        assert detail_response.data["problem_status"] == 2
        assert detail_response.data["status"] == 1
        assert (
            detail_response.data["export_country"]
            == "66b795e0-ad71-4a65-9fa6-9f1e97e86d67"
        )
        assert detail_response.data["sectors_affected"] is True
        assert detail_response.data["sectors"] == [
            "af959812-6095-e211-a939-e4115bead28a",
            "9538cecc-5f95-e211-a939-e4115bead28a",
        ]
        assert detail_response.data["product"] == "Some product"
        assert detail_response.data["source"] == "OTHER"
        assert detail_response.data["other_source"] == "Other source"
        assert detail_response.data["barrier_title"] == "Some title"
        assert detail_response.data["summary"] == "Some summary"
        stage_1 = [
            d for d in detail_response.data["progress"] if d["stage_code"] == "1.1"
        ]
        assert stage_1[0]["status_desc"] == "COMPLETED"
        stage_2 = [
            d for d in detail_response.data["progress"] if d["stage_code"] == "1.2"
        ]
        assert stage_2[0]["status_desc"] == "COMPLETED"
        stage_3 = [
            d for d in detail_response.data["progress"] if d["stage_code"] == "1.3"
        ]
        assert stage_3[0]["status_desc"] == "COMPLETED"
        stage_4 = [
            d for d in detail_response.data["progress"] if d["stage_code"] == "1.4"
        ]
        assert stage_4[0]["status_desc"] == "COMPLETED"

        submit_url = reverse("submit-report", kwargs={"pk": instance.id})
        submit_response = self.api_client.put(submit_url, format="json", data={})
        assert submit_response.status_code == status.HTTP_200_OK

    def test_submit_completed_report_3(self):
        url = reverse("list-reports")
        response = self.api_client.post(
            url,
            format="json",
            data={
                "problem_status": 2,
                "status_date": "2018-09-10",
                "status": 4,
                "export_country": "66b795e0-ad71-4a65-9fa6-9f1e97e86d67",
                "sectors_affected": True,
                "sectors": [
                    "af959812-6095-e211-a939-e4115bead28a",
                    "9538cecc-5f95-e211-a939-e4115bead28a",
                ],
                "product": "Some product",
                "source": "OTHER",
                "other_source": "Other source",
                "barrier_title": "Some title",
                "summary": "Some summary",
                "status_summary": "some status summary",
            },
        )

        assert response.status_code == status.HTTP_201_CREATED
        instance = BarrierInstance.objects.first()
        assert response.data["id"] == str(instance.id)

        detail_url = reverse("get-report", kwargs={"pk": instance.id})
        detail_response = self.api_client.get(detail_url)
        assert detail_response.status_code == status.HTTP_200_OK
        assert detail_response.data["problem_status"] == 2
        assert detail_response.data["status_date"] == "2018-09-10"
        assert detail_response.data["status"] == 4

        assert (
            detail_response.data["export_country"]
            == "66b795e0-ad71-4a65-9fa6-9f1e97e86d67"
        )
        assert detail_response.data["sectors_affected"] is True
        assert detail_response.data["sectors"] == [
            "af959812-6095-e211-a939-e4115bead28a",
            "9538cecc-5f95-e211-a939-e4115bead28a",
        ]
        assert detail_response.data["product"] == "Some product"
        assert detail_response.data["source"] == "OTHER"
        assert detail_response.data["other_source"] == "Other source"
        assert detail_response.data["barrier_title"] == "Some title"
        assert detail_response.data["summary"] == "Some summary"
        stage_1 = [
            d for d in detail_response.data["progress"] if d["stage_code"] == "1.1"
        ]
        assert stage_1[0]["status_desc"] == "COMPLETED"
        stage_2 = [
            d for d in detail_response.data["progress"] if d["stage_code"] == "1.2"
        ]
        assert stage_2[0]["status_desc"] == "COMPLETED"
        stage_3 = [
            d for d in detail_response.data["progress"] if d["stage_code"] == "1.3"
        ]
        assert stage_3[0]["status_desc"] == "COMPLETED"
        stage_4 = [
            d for d in detail_response.data["progress"] if d["stage_code"] == "1.4"
        ]
        assert stage_4[0]["status_desc"] == "COMPLETED"

        submit_url = reverse("submit-report", kwargs={"pk": instance.id})
        submit_response = self.api_client.put(submit_url, format="json", data={})
        assert submit_response.status_code == status.HTTP_200_OK

    def test_report_check_reference_code(self):
        url = reverse("list-reports")
        response = self.api_client.post(
            url,
            format="json",
            data={
                "product": "Some product",
                "source": "GOVT",
                "barrier_title": "Some title",
                "summary": "Some summary",
            },
        )

        assert response.status_code == status.HTTP_201_CREATED
        instance = BarrierInstance.objects.first()
        assert response.data["id"] == str(instance.id)

        detail_url = reverse("get-report", kwargs={"pk": instance.id})
        detail_response = self.api_client.get(detail_url)
        assert detail_response.status_code == status.HTTP_200_OK
        assert detail_response.data["product"] == "Some product"
        assert detail_response.data["source"] == "GOVT"
        assert detail_response.data["barrier_title"] == "Some title"
        assert detail_response.data["summary"] == "Some summary"
        assert detail_response.data["code"] != ""

    def test_report_deletion(self):
        url = reverse("list-reports")
        response = self.api_client.post(
            url,
            format="json",
            data={
                "product": "Some product",
                "source": "GOVT",
                "barrier_title": "Some title",
                "summary": "Some summary",
            },
        )

        assert response.status_code == status.HTTP_201_CREATED
        instance = BarrierInstance.objects.first()
        assert response.data["id"] == str(instance.id)

        detail_url = reverse("get-report", kwargs={"pk": instance.id})
        detail_response = self.api_client.get(detail_url)
        assert detail_response.status_code == status.HTTP_200_OK

        detail_response = self.api_client.delete(detail_url)
        assert detail_response.status_code == status.HTTP_204_NO_CONTENT

    def _test_report_deletion_failure(self):
        a_user_1 = create_test_user(
            first_name="", last_name="", email="", username="Test_1@Useri.com"
        )
        list_report_url = reverse("list-reports")
        api_client_1 = self.create_api_client(user=a_user_1)

        a_user_2 = create_test_user(
            first_name="", last_name="", email="", username="Test_2@Useri.com"
        )
        list_report_url = reverse("list-reports")
        api_client_2 = self.create_api_client(user=a_user_2)

        url = reverse("list-reports")
        response = api_client_1.post(
            url,
            format="json",
            data={
                "product": "Some product",
                "source": "GOVT",
                "barrier_title": "Some title",
                "summary": "Some summary",
            },
        )

        assert response.status_code == status.HTTP_201_CREATED
        instance = BarrierInstance.objects.first()
        assert response.data["id"] == str(instance.id)

        detail_url = reverse("get-report", kwargs={"pk": instance.id})
        detail_response = self.api_client_2.get(detail_url)
        assert detail_response.status_code == status.HTTP_200_OK

        detail_response = api_client_2.delete(detail_url)
        assert detail_response.status_code == status.HTTP_403_FORBIDDEN
