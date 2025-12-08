from django.contrib import admin
from django.utils.html import format_html
from .models import Lead, ChatbotLead, WebsiteLead, NewsletterSubscriber

# --- 1. CHATBOT LEAD ADMIN (Customized) ---
@admin.register(ChatbotLead)
class ChatbotLeadAdmin(admin.ModelAdmin):
    list_display = (
        "name", 
        "email", 
        "phone", 
        "display_service",   # Interested Service
        "display_message",   # Message
        "display_date"       # Received On
    )
    
    search_fields = ("name", "email", "phone", "service", "sub_services")
    list_filter = ("service", "created_at")
    ordering = ("-created_at",)
    
    # Read-only fields for detail view
    readonly_fields = ("created_at", "source", "message", "sub_services", "timeline")

    def get_queryset(self, request):
        return super().get_queryset(request).filter(source='chatbot')

    @admin.display(description='Interested Service')
    def display_service(self, obj):
        if not obj.service:
            return "-"
        return format_html(
            '<span style="color: #1565c0; font-weight: bold;">{}</span>',
            obj.service
        )

    @admin.display(description='Message')
    def display_message(self, obj):
        if obj.message and len(obj.message) > 50:
            return obj.message[:50] + "..."
        return obj.message

    @admin.display(description='Received On')
    def display_date(self, obj):
        return obj.created_at.strftime("%d %b %Y, %H:%M")


# --- 2. WEBSITE LEAD ADMIN ---
@admin.register(WebsiteLead)
class WebsiteLeadAdmin(admin.ModelAdmin):
    # Added 'timeline' to list display
    list_display = ("name", "company", "email", "service", "timeline", "created_at") 
    
    # Added 'timeline' to filters
    list_filter = ("service", "timeline", "created_at")
    
    # Added 'sub_services' to search
    search_fields = ("name", "email", "company", "sub_services")
    
    readonly_fields = ("created_at", "source", "sub_services", "timeline")
    ordering = ("-created_at",)

    def get_queryset(self, request):
        return super().get_queryset(request).filter(source='website')


# --- 3. ALL LEADS (Main Model) ---
@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "source", "service", "created_at")
    list_filter = ("source", "created_at")
    search_fields = ("name", "email", "sub_services")
    ordering = ("-created_at",)


# --- 4. NEWSLETTER SUBSCRIBERS ---
@admin.register(NewsletterSubscriber)
class NewsletterSubscriberAdmin(admin.ModelAdmin):
    list_display = ('email', 'subscribed_at')
    search_fields = ('email',)
    ordering = ('-subscribed_at',)