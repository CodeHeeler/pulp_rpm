from django.conf.urls import url

from .views import ApplicabilityView


urlpatterns = [
    url(r'^pulp/api/v3/rpm/applicability/$', ApplicabilityView.as_view({'post': 'create'}))
]
