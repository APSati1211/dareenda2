from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin
from .models import ContactMessage, ContactPage, OfficeAddress, Ticket

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "created_at")
    search_fields = ("name", "email", "message")
    readonly_fields = ("created_at",)

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('id', 'subject', 'email', 'priority', 'status', 'created_at')
    list_filter = ('status', 'priority')
    search_fields = ('subject', 'email', 'description')
    list_editable = ('status', 'priority')
    readonly_fields = ('created_at',)

@admin.register(ContactPage)
class ContactPageAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return ContactPage.objects.count() == 0

@admin.register(OfficeAddress)
class OfficeAddressAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('title', 'email', 'order')