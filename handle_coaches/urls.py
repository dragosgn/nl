from django.conf.urls import url, include
from . import views
from rest_framework.routers import DefaultRouter


# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'coaches_api', views.CoachViewSet)

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^coacheslist/$', views.coachesList, name='coacheslist'),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^coacheslist/(?P<coach_id>[0-9]+)$', views.coachProfile, name='coachdetail'),

]