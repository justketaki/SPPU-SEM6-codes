import re

def chatbot_response(user_input):
    user_input = user_input.lower()

    responses = {
        r"\b(1|hello|hi|hey)\b": "Hello! Welcome to IFB Washing Machine Service Centre. How can I assist you today?",
        r"\b(2|how are you)\b": "I'm a service bot, here to help you with your washing machine service and support.",
        r"\b(3|service request|repair|fix)\b": "To register a service request, please provide your machine model and issue description.",
        r"\b(4|cancel service|cancel request)\b": "To cancel a service request, please provide your service request number.",
        r"\b(5|status|service status)\b": "Please share your service request number to check the current status.",
        r"\b(6|warranty)\b": "Please share your machine model to check warranty status and service eligibility.",
        r"\b(7|payment options|payment)\b": "Service charges can be paid via cash, card, or UPI once the repair is completed.",
        r"\b(8|installation)\b": "For new machine installation, please provide your purchase invoice and preferred appointment date.",
        r"\b(9|maintenance tips|care)\b": "Regular cleaning and descaling keep your machine in top condition. Would you like a maintenance guide?",
        r"\b(10|thank you|thanks)\b": "You are welcome. Let me know if you need any more help.",
        r"\b(11|contact|help)\b": "You can contact our support team at ifbservice@ifbglobal.com or call 1800-3000-5678.",
        r"\b(12|spare parts|parts)\b": "We provide genuine IFB spare parts. Please mention the part you need for availability confirmation.",
        r"\b(13|service plans|amc)\b": "We offer Annual Maintenance Contracts (AMC) for hassle-free service. Would you like to know the plans?",
        r"\b(14|machine upgrade|exchange)\b": "We offer exchange programs on old machines. Would you like to explore upgrade options?",
        r"\b(15|exit|bye)\b": "Goodbye! Thank you for contacting IFB Washing Machine Service Centre.",
    }

    # Check user input against each pattern
    for pattern, response in responses.items():
        if re.search(pattern, user_input):
            return response

    # Default fallback if no pattern matches
    return "I am sorry, I did not understand that. Could you please rephrase your query?"

# Chatbot interaction loop
print("Welcome to IFB Washing Machine Service Centre Chatbot. Type 'exit' to end the conversation.")
print("\nMenu:\n1. Greet\n2. Ask Bot's Status\n3. Register Service Request\n4. Cancel Service Request\n5. Service Status\n6. Warranty Details\n7. Payment Options\n8. Installation Request\n9. Maintenance Tips\n10. Thank You\n11. Contact Support\n12. Spare Parts Inquiry\n13. Service Plans (AMC)\n14. Machine Upgrade or Exchange\n15. Exit")

while True:
    user_message = input("\nYou: ")
    if user_message.lower() in ["bye", "exit", "15"]:
        print("Chatbot: Goodbye! Thank you for contacting IFB Washing Machine Service Centre.")
        break
    response = chatbot_response(user_message)
    print("Chatbot:", response)
