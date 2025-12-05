from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter

# --- IMPORTS ---
from cms.views import (
    SiteContentViewSet, 
    home_page_content, 
    CaseStudyViewSet, 
    ResourceViewSet, 
    ServiceViewSet, 
    PageViewSet
)
from blog.views import BlogPostViewSet, BlogCategoryViewSet
from leads.views import LeadViewSet, NewsletterSubscriberViewSet, chat_flow_handler
from contact.views import ContactViewSet
from careers.views import JobOpeningViewSet, JobApplicationViewSet
# from stakeholders.views import StakeholderViewSet  <-- Iski ab zarurat nahi yahan

# --- ROUTER REGISTRATION ---
router = DefaultRouter()

# CMS Endpoints
router.register(r'sitecontent', SiteContentViewSet)
router.register(r'case-studies', CaseStudyViewSet)
router.register(r'resources', ResourceViewSet)
router.register(r'services', ServiceViewSet)
router.register(r'pages', PageViewSet)

# Blog Endpoints
router.register(r'blogs', BlogPostViewSet, basename='blog')
router.register(r'blog-categories', BlogCategoryViewSet, basename='blog-category')

# Lead & Contact Endpoints
router.register(r'leads', LeadViewSet, basename='lead')
router.register(r'subscribers', NewsletterSubscriberViewSet)
router.register(r'contact', ContactViewSet, basename='contact')

# Career Endpoints
router.register(r'jobs', JobOpeningViewSet)
router.register(r'apply', JobApplicationViewSet)

# Stakeholders Endpoint
# router.register(r'stakeholders', StakeholderViewSet) <-- YE LINE HATA DI KYUNKI AB YE 'stakeholders.urls' MEIN HAI

urlpatterns = [
    path("admin/", admin.site.urls),
    
    # Router URLs (CRUD APIs)
    path("api/", include(router.urls)),
    
    # Custom Handlers
    path("api/chatbot-flow/", chat_flow_handler),
    path("api/home-page-content/", home_page_content),
    
    # Theme URLs
    path("api/", include("theme.urls")),
    
    # --- CUSTOM PAGES URLs ---
    path("api/", include("homepage.urls")),       
    path("api/about-page-data/", include("about.urls")), 
    path("api/", include("resources_page.urls")), 
    path("api/", include("lead_system_page.urls")), 
    path("api/legal/", include("legal.urls")),    
    path("api/", include("services_page.urls")),  
    path('api/', include('careers.urls')),
    path("api/", include("contact.urls")),
    
    # --- NEW: Solutions Page Logic included here ---
    path("api/", include("stakeholders.urls")), # <--- Ye line add karni zaroori thi
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)