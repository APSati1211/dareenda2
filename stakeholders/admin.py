from django.contrib import admin
from django.utils.html import format_html
from adminsortable2.admin import SortableAdminMixin
from .models import Stakeholder, SolutionsPage

@admin.register(Stakeholder)
class StakeholderAdmin(SortableAdminMixin, admin.ModelAdmin):
    # ID shuru mein dikhegi, jis par click karke full edit khulega
    list_display = ('id', 'title', 'icon_preview', 'desc_preview', 'order')
    
    # Ye fields seedhe list mein edit ho jayenge
    list_editable = ('title', 'order') 
    
    # ID par click karne se form khulega
    list_display_links = ('id',)
    
    search_fields = ('title', 'description')

    # Description ka chhota preview dikhane ke liye function
    def desc_preview(self, obj):
        return obj.description[:75] + "..." if obj.description else "-"
    desc_preview.short_description = "Description"

    # Icon/Image ka preview dikhane ke liye function
    def icon_preview(self, obj):
        # FIX: 'obj.icon' ki jagah 'obj.image' use kiya
        if obj.image:
            return format_html('<img src="{}" style="width: 40px; height: 40px; object-fit: contain;" />', obj.image.url)
        return "❌ No Image"
    icon_preview.short_description = "Image Preview"

@admin.register(SolutionsPage)
class SolutionsPageAdmin(admin.ModelAdmin):
    # Restrict to one instance to act as a singleton
    def has_add_permission(self, request):
        return not SolutionsPage.objects.exists()