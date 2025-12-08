from rest_framework import viewsets, mixins
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import ContactMessage, ContactPage, OfficeAddress, Ticket
from .serializers import ContactSerializer, ContactPageSerializer, OfficeAddressSerializer, TicketSerializer

# Form Submission View
class ContactViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = ContactMessage.objects.all()
    serializer_class = ContactSerializer

# Ticket Submission View
class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all().order_by('-created_at')
    serializer_class = TicketSerializer

# Page Data View
class ContactPageDataView(APIView):
    def get(self, request):
        content = ContactPage.objects.first()
        addresses = OfficeAddress.objects.all()
        
        return Response({
            "content": ContactPageSerializer(content).data if content else None,
            "addresses": OfficeAddressSerializer(addresses, many=True).data,
        })