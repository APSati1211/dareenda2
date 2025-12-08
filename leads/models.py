from django.db import models

class Lead(models.Model):
    name = models.CharField(max_length=200)
    company = models.CharField(max_length=200, blank=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=30, blank=True)
    
    # --- Updated Service Fields ---
    service = models.CharField(max_length=200, blank=True, help_text="Main Service Category")
    sub_services = models.TextField(blank=True, help_text="Comma-separated list of selected sub-services")
    timeline = models.CharField(max_length=100, blank=True, help_text="When is the service required?")
    # ------------------------------

    message = models.TextField(blank=True)
    source = models.CharField(max_length=100, blank=True, default="website")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # Shows Name, Service, and Date in Admin dropdowns
        return f"{self.name} ({self.service}) - {self.created_at.strftime('%Y-%m-%d')}"

class ChatbotLeadManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(source='chatbot')

class ChatbotLead(Lead):
    objects = ChatbotLeadManager()
    class Meta:
        proxy = True
        verbose_name = 'Chatbot Lead'
        verbose_name_plural = 'Chatbot Leads'

class WebsiteLeadManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(source='website')

class WebsiteLead(Lead):
    objects = WebsiteLeadManager()
    class Meta:
        proxy = True
        verbose_name = 'Website Lead'
        verbose_name_plural = 'Website Leads'

class NewsletterSubscriber(models.Model):
    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email