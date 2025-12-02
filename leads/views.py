from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from theme.models import ChatbotFlowStep
from .models import Lead, NewsletterSubscriber
from .serializers import LeadSerializer, NewsletterSubscriberSerializer
import logging

# Logger setup for debugging
logger = logging.getLogger(__name__)

# --- 1. Lead ViewSet ---
class LeadViewSet(viewsets.ModelViewSet):
    queryset = Lead.objects.all().order_by("-created_at")
    serializer_class = LeadSerializer

# --- 2. Newsletter Subscriber ViewSet ---
class NewsletterSubscriberViewSet(viewsets.ModelViewSet):
    queryset = NewsletterSubscriber.objects.all().order_by('-subscribed_at')
    serializer_class = NewsletterSubscriberSerializer

# --- 3. CHATBOT FLOW HANDLER (UPDATED) ---
@api_view(['POST'])
def chat_flow_handler(request):
    """
    Handles the sequential, CMS-configured chatbot flow.
    Saves answers in session, validates required fields, and generates a Lead at the end.
    """
    try:
        # Request data extraction
        current_field = request.data.get('current_field') 
        answer = request.data.get('answer')
        
        # Session retrieval
        flow_data = request.session.get('chatbot_flow_data', {})
        
        # Debugging: Print current flow data to console
        print(f"Chatbot Incoming: Field={current_field}, Answer={answer}")
        print(f"Current Session Data: {flow_data}")

        # --- STEP 1: VALIDATION ---
        if current_field:
            current_step_obj = ChatbotFlowStep.objects.filter(field_to_save=current_field).first()
            
            # Agar field required hai aur user ne answer nahi diya (Empty string)
            if current_step_obj and current_step_obj.is_required and not answer:
                return Response({
                    "next_question": current_step_obj.question_text, 
                    "next_field": current_field,
                    "is_complete": False,
                    "error": "This field is required. Please provide an answer." 
                })

        # --- STEP 2: SAVE ANSWER ---
        if current_field:
            # Save answer even if it's empty (for optional fields)
            flow_data[current_field] = answer if answer else ""
            
            request.session['chatbot_flow_data'] = flow_data 
            request.session.modified = True # <--- CRITICAL FIX: Force Django to save session
            
        # --- STEP 3: DETERMINE NEXT STEP ---
        last_order = 0
        if current_field:
            last_step = ChatbotFlowStep.objects.filter(field_to_save=current_field).first()
            if last_step:
                last_order = last_step.step_order
        
        # Agla step dhundo jiska order pichle wale se bada ho
        next_step = ChatbotFlowStep.objects.filter(step_order__gt=last_order).order_by('step_order').first()

        # --- STEP 4: RESPONSE OR LEAD GENERATION ---
        if next_step:
            return Response({
                "next_question": next_step.question_text,
                "next_field": next_step.field_to_save,
                "is_complete": False
            })
        else:
            # --- FINAL STEP: CREATE LEAD ---
            print("Creating Lead with Data:", flow_data) # Debug print

            # Extract specific fields with fallbacks
            lead_name = flow_data.get('name', 'Unknown User')
            lead_email = flow_data.get('email', '')
            lead_phone = flow_data.get('phone', '')
            lead_service = flow_data.get('service', 'General Inquiry')
            lead_message = flow_data.get('message', 'Chatbot Inquiry') 
            
            # Additional company field if you ask for it
            lead_company = flow_data.get('company', '') 

            # Save to Database
            new_lead = Lead.objects.create(
                name=lead_name,
                email=lead_email,
                phone=lead_phone,
                service=lead_service,
                message=lead_message,
                company=lead_company,
                source="chatbot"
            )
            print(f"Lead Created Successfully: ID {new_lead.id}")

            # Clear session after successful save
            if 'chatbot_flow_data' in request.session:
                del request.session['chatbot_flow_data']
                request.session.modified = True
            
            return Response({
                "next_question": f"Thank you, {lead_name}! We have received your details and will contact you shortly.",
                "next_field": None,
                "is_complete": True,
                "action": "lead_captured"
            })
        
    except Exception as e:
        print(f"Chatbot Critical Error: {e}")
        
        # Agar koi error aaye to session clear karke restart karo
        if 'chatbot_flow_data' in request.session:
            del request.session['chatbot_flow_data']
            request.session.modified = True
        
        first_step = ChatbotFlowStep.objects.order_by('step_order').first()
        return Response({
            "error": "System encountered an error. Restarting chat...",
            "next_question": first_step.question_text if first_step else "Welcome to XpertAI. How can I help?",
            "next_field": first_step.field_to_save if first_step else "name",
            "is_complete": False
        })