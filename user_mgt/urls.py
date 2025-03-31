from rest_framework import routers

from user_mgt.views import MeViewSet

router = routers.DefaultRouter()
router.register('me', MeViewSet, basename='me')