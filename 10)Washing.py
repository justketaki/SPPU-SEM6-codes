import re

# State management variables
last_question = None
booking_in_progress = False
booking_details = {}

def ifb_service_chatbot(user_input):
    global last_question, booking_in_progress, booking_details
    user_input = user_input.lower()

    if booking_in_progress:
        if "name" not in booking_details:
            booking_details["name"] = user_input.title()
            return "Please provide your phone number."
        elif "phone" not in booking_details:
            booking_details["phone"] = user_input
            return "Please provide your washing machine model number."
        elif "model" not in booking_details:
            booking_details["model"] = user_input.upper()
            booking_in_progress = False
            confirmation_message = (
                f"Thank you {booking_details['name']}! Your service request for model {booking_details['model']} "
                f"has been registered. We will contact you shortly at {booking_details['phone']}."
            )
            booking_details.clear()
            return confirmation_message

    # Service list when user says 'yes'
    service_list = """
Here are the services we offer:
- Book a Technician Visit
- Washing Machine Installation
- Washing Machine Repair
- Routine Maintenance Service
- Spare Parts Replacement (Motor, Drum, Control Panel)
- Cleaning & Descaling Service
Would you like to book a service? (yes/no)
"""

    responses = {
        r"\b(hello|hi|hey)\b": "Hello! Welcome to IFB Washing Machine Service Centre. How can I assist you today?",
        r"\b(service|repair|technician|maintenance|fix)\b": "We provide technician visits, repairs, and maintenance. Would you like to see available service options? (yes/no)",
        r"\b(installation|setup)\b": "We offer installation and demo services. Would you like to book installation? (yes/no)",
        r"\b(complaint|issue|problem|not working|error)\b": "Sorry to hear that. Would you like to book a technician visit? (yes/no)",
        r"\b(warranty|extended warranty|amc|annual maintenance contract)\b": "We offer extended warranty and AMC plans. Would you like to know more? (yes/no)",
        r"\b(spare parts|parts replacement|motor|drum|control panel)\b": "We provide genuine IFB spare parts. Would you like to request a part replacement? (yes/no)",
        r"\b(cleaning|descaling|drum cleaning)\b": "We offer professional cleaning and descaling services. Would you like to book a cleaning service? (yes/no)",
        r"\b(payment options|how to pay|payment methods)\b": "We accept UPI, cards, net banking, and cash after service.",
        r"\b(price|service cost|charges|fees)\b": "Service charges start from ₹500 depending on the type of service. Inspection charges are adjustable in final bill.",
        r"\b(track service|service status|where is technician)\b": "You can track your technician's live status through the SMS link sent to your registered number.",
        r"\b(cancel booking|reschedule|change appointment)\b": "To reschedule or cancel, please call our helpline at 1800-3000-5678 with your booking ID.",
        r"\b(customer support|talk to agent|contact)\b": "You can call us anytime at 1800-3000-5678 or email service@ifbglobal.com.",
        r"\b(thank you|thanks)\b": "You're welcome! Happy to help. Anything else you need?",
        r"\b(bye|exit)\b": "Goodbye! Thanks for contacting IFB Service Centre. Have a great day!"
    }

    if user_input in ["yes", "yeah", "yup", "sure"]:
        if last_question == "service_options":
            last_question = None
            booking_in_progress = True
            return "Great! Please provide your name to start the booking."
        else:
            return "Can you please specify what you are saying 'yes' to?"

    elif user_input in ["no", "nah", "nope"]:
        if last_question == "service_options":
            last_question = None
            return "No problem! Let me know if you need any other assistance."
        else:
            return "Okay, let me know if you need anything else!"

    # Match patterns
    for pattern, response in responses.items():
        if re.search(pattern, user_input):
            if "would you like" in response.lower():
                last_question = "service_options"
            else:
                last_question = None
            return response

    return "I'm sorry, I didn't catch that. Could you please rephrase your query?"

print("Welcome to IFB Washing Machine Service Centre Chatbot! Type 'exit' to end the conversation.")

while True:
    user_message = input("You: ")
    if user_message.lower() in ["bye", "exit"]:
        print("Chatbot: Goodbye! Thanks for contacting IFB Service Centre!")
        break
    response = ifb_service_chatbot(user_message)
    print("Chatbot:", response)

