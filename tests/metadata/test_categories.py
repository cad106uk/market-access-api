from api.core.test_utils import APITestMixin

from api.metadata.models import Category


class TestCategories(APITestMixin):
    def test_categories_count(self):
        categories_count = Category.objects.count()
        assert categories_count == 33

    def test_categories_goods_count(self):
        categories_count = Category.goods.count()
        assert categories_count == 26

    def test_categories_services_count(self):
        categories_count = Category.services.count()
        assert categories_count == 22
