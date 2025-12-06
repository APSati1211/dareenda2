from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .sections import get_section_slugs
from .models import SiteContent, CaseStudy, Resource, Service, Page
from .serializers import (
    SiteContentSerializer, CaseStudySerializer, 
    ResourceSerializer, ServiceSerializer
)
from rest_framework import serializers 

@api_view(['GET'])
def get_section_choices(request, page):
    """Returns the allowed section slugs for a given page."""
    sections = get_section_slugs(page)
    return Response(sections)

class SiteContentViewSet(viewsets.ModelViewSet):
    queryset = SiteContent.objects.all()
    serializer_class = SiteContentSerializer

    def get_queryset(self):
        qs = SiteContent.objects.all()
        page = self.request.query_params.get("page")
        if page:
            qs = qs.filter(page=page)
        return qs

@api_view(['GET'])
def home_page_content(request):
    """Returns all the site content for the home page."""
    qs = SiteContent.objects.filter(page="home")
    # FIX: context={'request': request} added here
    serializer = SiteContentSerializer(qs, many=True, context={'request': request})
    return Response(serializer.data)

class CaseStudyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CaseStudy.objects.all().order_by('-created_at')
    serializer_class = CaseStudySerializer

class ResourceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Resource.objects.all().order_by('-created_at')
    serializer_class = ResourceSerializer

class ServiceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Service.objects.all().order_by('order')
    serializer_class = ServiceSerializer
    lookup_field = 'slug'

# --- PAGE VIEWSET FOR NAVBAR ---
class PageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = ['title', 'slug', 'page_order']

class PageViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Page.objects.all().order_by('page_order')
    serializer_class = PageSerializer