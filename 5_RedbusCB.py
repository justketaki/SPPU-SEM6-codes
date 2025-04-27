import re

def chatbot_response(user_input):
    user_input = user_input.lower()

    responses = {
        r"\b(1|hello|hi|hey)\b": "Hello! Welcome to RedBus. How can I assist you with your bus travel today?",
        r"\b(2|how are you)\b": "I'm just a bot, but I'm here to help you with booking and managing your bus tickets!",
        r"\b(3|book|reserve|ticket)\b": "To book a bus ticket, please provide your source, destination, and travel date.",
        r"\b(4|cancel|cancellation)\b": "To cancel your booking, please provide your booking ID.",
        r"\b(5|status|booking status)\b": "Please provide your booking ID to check the status of your reservation.",
        r"\b(6|refund)\b": "Refunds are processed within 7 business days. Please provide your booking ID to check the refund status.",
        r"\b(7|payment options|pay)\b": "We accept credit/debit cards, UPI, and net banking for payment. Which method would you prefer?",
        r"\b(8|bus timings|schedule)\b": "Please provide your source and destination to check the bus timings.",
        r"\b(9|route|location)\b": "Our buses operate between major cities. Please specify your source and destination for route details.",
        r"\b(10|thank you|thanks)\b": "You're welcome! Let me know if you need any more assistance.",
        r"\b(11|contact|help)\b": "You can reach our support team at support@redbus.com or call us at 1800-123-4567.",
        r"\b(12|available buses)\b": "We have a variety of buses available from AC to non-AC. What type of bus are you looking for?",
        r"\b(13|promotions|offers)\b": "We have ongoing promotions with discounts up to 25%! Would you like to know more?",
        r"\b(14|discount)\b": "We have seasonal discounts on bookings made in advance. Let me know your travel details to check the discount.",
        r"\b(15|booking details)\b": "To view your booking details, please provide your booking ID.",
        r"\b(16|view ticket)\b": "Please share your booking ID to view or print your ticket.",
        r"\b(17|pick up point)\b": "Your bus pick-up point will be at the city bus station. Would you like to confirm the exact location?",
        r"\b(18|drop off point)\b": "Your bus drop-off point will be the main terminal in the destination city. Would you like to confirm it?",
        r"\b(19|travel insurance)\b": "We offer travel insurance with your booking. Would you like to opt for it?",
        r"\b(20|schedule change)\b": "If there is any change in your bus schedule, you will be notified via SMS or email.",
        r"\b(21|exit|bye)\b": "Goodbye! Have a safe journey. ✨",
    }

    # Check the user input against each pattern
    for pattern, response in responses.items():
        if re.search(pattern, user_input):
            return response

    # Default response if no pattern matches
    return "I am sorry, I didn't understand that. Can you rephrase or ask about a specific booking service?"

# Chatbot interaction loop
print("Welcome to RedBus Chatbot! Type 'exit' to end the conversation.")

while True:
    user_message = input("You: ")
    if user_message.lower() in ["bye", "exit"]:
        print("Chatbot: Goodbye! Have a safe journey. ✨")
        break
    response = chatbot_response(user_message)
    print("Chatbot:", response)
