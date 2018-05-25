from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path

from api.ping.views import ping
from api.user.views import who_am_i
from api.barriers.views import BarrierList, BarrierDetail
from api.metadata.views import MetadataView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path('ping.xml', ping, name='ping'),
    path('whoami/', who_am_i, name='who_am_i'),
    url(r'^barriers/$', BarrierList.as_view()),
    path('barriers/<int:pk>/', BarrierDetail.as_view()),
    path('metadata/', MetadataView.as_view()),
]
