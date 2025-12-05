from django.core.management.base import BaseCommand
from stakeholders.models import Stakeholder, SolutionsPage

class Command(BaseCommand):
    help = "Seeds the Solutions Page content and Stakeholder cards"

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.WARNING("Cleaning old Solutions data..."))
        
        # 1. Clear old data
        Stakeholder.objects.all().delete()
        SolutionsPage.objects.all().delete()

        # 2. Create Page Content (Hero & CTA) with ALL required fields
        SolutionsPage.objects.create(
            hero_title="Our Ecosystem",
            hero_subtitle="Connecting Clients, Experts, and Learners in one unified financial platform.",
            cta_title="Ready to find your place?",
            cta_text="Join XpertAI today. Whether you need service, want to work, or want to learn - we have a solution for you.",
            cta_btn_primary="Get Started",     # Ye field missing tha
            cta_btn_secondary="Contact Us"     # Ye bhi add kar diya safety ke liye
        )

        # 3. Create Solution Cards
        cards_data = [
            {
                "title": "Clients",
                "description": "Businesses and Startups seeking Virtual CFOs, Auditors, and Tax Experts for end-to-end financial management.",
                "icon": "Building2",
                "order": 1
            },
            {
                "title": "Professionals",
                "description": "Chartered Accountants, CS, and CMAs looking for high-value projects and verified global clients.",
                "icon": "Briefcase",
                "order": 2
            },
            {
                "title": "Freelancers / Freshers",
                "description": "Emerging financial talent looking for internships, gig projects, and mentorship opportunities.",
                "icon": "GraduationCap",
                "order": 3
            },
            {
                "title": "Trainers",
                "description": "Subject Matter Experts delivering specialized financial training, workshops, and certifications.",
                "icon": "Presentation",
                "order": 4
            },
            {
                "title": "Training Institutes",
                "description": "Educational organizations partnering for curriculum support, placement assistance, and practical exposure.",
                "icon": "School",
                "order": 5
            }
        ]

        for card in cards_data:
            Stakeholder.objects.create(
                title=card["title"],
                description=card["description"],
                icon_name=card["icon"],
                order=card["order"]
            )

        self.stdout.write(self.style.SUCCESS(f"Successfully populated Solutions Page with {len(cards_data)} cards!"))