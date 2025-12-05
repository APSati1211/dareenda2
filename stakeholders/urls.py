from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import StakeholderViewSet, SolutionsPageDataView

router = DefaultRouter()
router.register(r'stakeholders', StakeholderViewSet)

urlpatterns = [
    path('solutions-page-data/', SolutionsPageDataView.as_view(), name='solutions-page-data'),
] + router.urls