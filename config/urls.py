from django.contrib import admin
from django.urls import path

from api.metadata.views import MetadataView
from api.ping.views import ping
from api.barriers.views import (
    barrier_count,
    BarrierList,
    BarrierDetail,
    BarrierInstanceInteraction,
    BarrierInstanceContributor,
    BarrierResolve,
    BarrierHibernate,
    BarrierOpen,
    BarrierStatusList,
    BarrierReportList,
    BarrierReportDetail,
    BarrierReportSubmit,
)
from api.user.views import who_am_i

urlpatterns = [
    path("admin", admin.site.urls),
    path("ping.xml", ping, name="ping"),
    path("whoami", who_am_i, name="who_am_i"),

    path("reports", BarrierReportList.as_view(), name="list-reports"),
    path("reports/<uuid:pk>", BarrierReportDetail.as_view()),
    path("reports/<uuid:pk>/submit", BarrierReportSubmit.as_view()),

    path("metadata", MetadataView.as_view()),

    path("barriers", BarrierList.as_view(), name="list-barriers"),
    path("barriers/count", barrier_count),
    path("barriers/<uuid:pk>", BarrierDetail.as_view()),
    path("barriers/<uuid:barrier_pk>/contributors", BarrierInstanceContributor.as_view()),
    path("barriers/<uuid:barrier_pk>/interactions", BarrierInstanceInteraction.as_view()),
    path("barriers/<uuid:pk>/resolve", BarrierResolve.as_view()),
    path("barriers/<uuid:pk>/hibernate", BarrierHibernate.as_view()),
    path("barriers/<uuid:pk>/open", BarrierOpen.as_view()),
    path("barriers/<uuid:barrier_pk>/statuses", BarrierStatusList.as_view()),
]
