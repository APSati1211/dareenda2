from django.core.management.base import BaseCommand
from legal.models import LegalPage, LegalPageSection

class Command(BaseCommand):
    help = 'Populates Legal Pages with dummy professional data'

    def handle(self, *args, **kwargs):
        self.stdout.write("Deleting old legal pages data...")
        # Purana data saaf karte hain taaki duplicate na ho
        LegalPage.objects.filter(slug__in=['privacy-policy', 'terms-and-conditions']).delete()

        # ==========================================
        # 1. PRIVACY POLICY
        # ==========================================
        self.stdout.write("Creating Privacy Policy...")
        pp = LegalPage.objects.create(
            title="Privacy Policy",
            slug="privacy-policy",
            description="At XpertAI, we value your privacy and are committed to protecting your personal data. This policy outlines our practices."
        )

        pp_sections = [
            ("1. Introduction", "Welcome to XpertAI. We respect your privacy and are committed to protecting your personal data. This privacy policy will inform you as to how we look after your personal data when you visit our website (regardless of where you visit it from) and tell you about your privacy rights and how the law protects you."),
            ("2. Information We Collect", "We may collect, use, store and transfer different kinds of personal data about you which we have grouped together follows: Identity Data, Contact Data, Financial Data, Transaction Data, Technical Data, Profile Data, Usage Data, and Marketing and Communications Data."),
            ("3. How We Use Your Data", "We will only use your personal data when the law allows us to. Most commonly, we will use your personal data in the following circumstances: Where we need to perform the contract we are about to enter into or have entered into with you; Where it is necessary for our legitimate interests."),
            ("4. Cookies and Tracking", "Our website uses cookies to distinguish you from other users of our website. This helps us to provide you with a good experience when you browse our website and also allows us to improve our site. You can set your browser to refuse all or some browser cookies."),
            ("5. Data Security", "We have put in place appropriate security measures to prevent your personal data from being accidentally lost, used or accessed in an unauthorized way, altered or disclosed. In addition, we limit access to your personal data to those employees, agents, contractors and other third parties who have a business need to know."),
            ("6. Data Retention", "We will only retain your personal data for as long as necessary to fulfill the purposes we collected it for, including for the purposes of satisfying any legal, accounting, or reporting requirements. To determine the appropriate retention period for personal data, we consider the amount, nature, and sensitivity of the personal data."),
            ("7. Third-Party Links", "This website may include links to third-party websites, plug-ins, and applications. Clicking on those links or enabling those connections may allow third parties to collect or share data about you. We do not control these third-party websites and are not responsible for their privacy statements."),
            ("8. Your Legal Rights", "Under certain circumstances, you have rights under data protection laws in relation to your personal data. These include the right to: Request access to your personal data; Request correction of your personal data; Request erasure of your personal data; Object to processing of your personal data."),
            ("9. International Transfers", "We share your personal data within the XpertAI Group. This will involve transferring your data outside the European Economic Area (EEA). Whenever we transfer your personal data out of the EEA, we ensure a similar degree of protection is afforded to it by ensuring at least one of the specific safeguards is implemented."),
            ("10. Children's Privacy", "Our Services do not address anyone under the age of 13. We do not knowingly collect personal identifiable information from children under 13. In the case we discover that a child under 13 has provided us with personal information, we immediately delete this from our servers."),
            ("11. Changes to This Policy", "We may update our Privacy Policy from time to time. We will notify you of any changes by posting the new Privacy Policy on this page. You are advised to review this Privacy Policy periodically for any changes. Changes to this Privacy Policy are effective when they are posted on this page."),
            ("12. Contact Us", "If you have any questions about this Privacy Policy, please contact us by email: support@xpertai.global or by visiting this page on our website: https://xpertai.global/contact.")
        ]

        for index, (head, content) in enumerate(pp_sections, 1):
            LegalPageSection.objects.create(legal_page=pp, heading=head, content=content, order=index)

        # ==========================================
        # 2. TERMS AND CONDITIONS
        # ==========================================
        self.stdout.write("Creating Terms and Conditions...")
        tc = LegalPage.objects.create(
            title="Terms and Conditions",
            slug="terms-and-conditions",
            description="Please read these terms and conditions carefully before using our service."
        )

        tc_sections = [
            ("1. Introduction", "These Terms and Conditions govern your use of our website located at xpertai.global operated by XpertAI. By accessing this website we assume you accept these terms and conditions. Do not continue to use XpertAI if you do not agree to take all of the terms and conditions stated on this page."),
            ("2. Intellectual Property Rights", "Other than the content you own, under these Terms, XpertAI and/or its licensors own all the intellectual property rights and materials contained in this Website. You are granted limited license only for purposes of viewing the material contained on this Website."),
            ("3. Restrictions", "You are specifically restricted from all of the following: publishing any Website material in any other media; selling, sublicensing and/or otherwise commercializing any Website material; publicly performing and/or showing any Website material; using this Website in any way that is or may be damaging to this Website."),
            ("4. User Content", "In these Website Standard Terms and Conditions, 'Your Content' shall mean any audio, video text, images or other material you choose to display on this Website. By displaying Your Content, you grant XpertAI a non-exclusive, worldwide irrevocable, sub licensable license to use, reproduce, adapt, publish, translate and distribute it."),
            ("5. No Warranties", "This Website is provided 'as is,' with all faults, and XpertAI express no representations or warranties, of any kind related to this Website or the materials contained on this Website. Also, nothing contained on this Website shall be interpreted as advising you."),
            ("6. Limitation of Liability", "In no event shall XpertAI, nor any of its officers, directors and employees, be held liable for anything arising out of or in any way connected with your use of this Website whether such liability is under contract. XpertAI, including its officers, directors and employees shall not be held liable for any indirect, consequential or special liability."),
            ("7. Indemnification", "You hereby indemnify to the fullest extent XpertAI from and against any and/or all liabilities, costs, demands, causes of action, damages and expenses arising in any way related to your breach of any of the provisions of these Terms."),
            ("8. Severability", "If any provision of these Terms is found to be invalid under any applicable law, such provisions shall be deleted without affecting the remaining provisions herein."),
            ("9. Variation of Terms", "XpertAI is permitted to revise these Terms at any time as it sees fit, and by using this Website you are expected to review these Terms on a regular basis."),
            ("10. Assignment", "The XpertAI is allowed to assign, transfer, and subcontract its rights and/or obligations under these Terms without any notification. However, you are not allowed to assign, transfer, or subcontract any of your rights and/or obligations under these Terms."),
            ("11. Governing Law & Jurisdiction", "These Terms will be governed by and interpreted in accordance with the laws of the State of Country, and you submit to the non-exclusive jurisdiction of the state and federal courts located in Country for the resolution of any disputes."),
            ("12. Termination", "We may terminate or suspend access to our Service immediately, without prior notice or liability, for any reason whatsoever, including without limitation if you breach the Terms. All provisions of the Terms which by their nature should survive termination shall survive termination.")
        ]

        for index, (head, content) in enumerate(tc_sections, 1):
            LegalPageSection.objects.create(legal_page=tc, heading=head, content=content, order=index)

        self.stdout.write(self.style.SUCCESS('Successfully populated Legal Pages with 12+ sections each!'))