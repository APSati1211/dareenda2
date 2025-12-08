from rest_framework import serializers
from .models import ContactMessage, ContactPage, OfficeAddress, Ticket

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = "__all__"

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = "__all__"
        read_only_fields = ['status', 'created_at']

class OfficeAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = OfficeAddress
        fields = "__all__"

class ContactPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactPage
        fields = "__all__"