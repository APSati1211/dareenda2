from rest_framework.views import APIView
from rest_framework.response import Response
from .models import (
    ServiceHero, ServiceProcess, ServiceFeature, 
    ServiceTestimonial, ServiceFAQ, ServiceCTA
)
from .serializers import (
    ServiceHeroSerializer, ServiceProcessSerializer, ServiceFeatureSerializer, 
    ServiceTestimonialSerializer, ServiceFAQSerializer, ServiceCTASerializer
)
# CMS App se Service List laane ke liye
from cms.models import Service
from cms.serializers import ServiceSerializer

class ServicePageDataView(APIView):
    def get(self, request):
        hero = ServiceHero.objects.first()
        cta = ServiceCTA.objects.first()
        
        return Response({
            "hero": ServiceHeroSerializer(hero, context={'request': request}).data if hero else None,
            "process": ServiceProcessSerializer(ServiceProcess.objects.all(), many=True, context={'request': request}).data,
            "features": ServiceFeatureSerializer(ServiceFeature.objects.all(), many=True, context={'request': request}).data,
            "testimonials": ServiceTestimonialSerializer(ServiceTestimonial.objects.all(), many=True, context={'request': request}).data,
            "faq": ServiceFAQSerializer(ServiceFAQ.objects.all(), many=True, context={'request': request}).data,
            "cta": ServiceCTASerializer(cta, context={'request': request}).data if cta else None,
            
            # Actual Services List (Dynamic) - Ye wala sabse important hai images ke liye
            "services_list": ServiceSerializer(Service.objects.all().order_by('order'), many=True, context={'request': request}).data
        })