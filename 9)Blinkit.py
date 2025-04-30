import re

def chatbot_response(user_input):
    user_input = user_input.lower()

    responses = {
        r"\b(1|hello|hi|hey)\b": "Hello! Welcome to Blink-IT. How can I help you today?",
        r"\b(2|how are you)\b": "I'm a chatbot ready to assist you with your grocery orders.",
        r"\b(3|order|buy|purchase)\b": "To place an order, please mention the item you wish to buy.",
        r"\b(4|cancel|cancellation)\b": "To cancel an order, please provide your order ID.",
        r"\b(5|status|order status)\b": "Please share your order ID to check the current status.",
        r"\b(6|refund)\b": "Refunds are processed within 3 to 5 business days. Please provide your order ID.",
        r"\b(7|payment options|payment)\b": "We accept UPI, credit/debit cards, and cash on delivery.",
        r"\b(8|delivery time|when)\b": "Most deliveries are completed within 10 to 30 minutes after placing the order.",
        r"\b(9|items available|products)\b": "We have fresh fruits, vegetables, dairy products, snacks, and daily essentials. What are you looking for?",
        r"\b(10|thank you|thanks)\b": "You are welcome. Let me know if you need further assistance.",
        r"\b(11|contact|help)\b": "You can contact our support team at support@blinkit.com or call 1800-222-5555.",
        r"\b(12|offers|discounts|promotions)\b": "We have exciting discounts and cashback offers. Would you like to know today's special offers?",
        r"\b(13|return|replace)\b": "We offer easy return and replacement for damaged or wrong items. Please share your order ID.",
        r"\b(14|membership|blinkit plus)\b": "Blink-IT Plus members get free delivery and exclusive offers. Would you like to join?",
        r"\b(15|exit|bye)\b": "Goodbye! Thank you for choosing Blink-IT.",
    }

    # Check user input against each pattern
    for pattern, response in responses.items():
        if re.search(pattern, user_input):
            return response

    # Default response if no match found
    return "I am sorry, I did not understand that. Can you please rephrase your query?"

# Chatbot interaction loop
print("Welcome to Blink-IT Chatbot. Type 'exit' to end the conversation.")
print("\nMenu:\n1. Greet\n2. Ask Bot's Status\n3. Place Order\n4. Cancel Order\n5. Order Status\n6. Refund Details\n7. Payment Options\n8. Delivery Time\n9. Available Items\n10. Thank You\n11. Contact Support\n12. Offers and Discounts\n13. Return or Replacement\n14. Membership\n15. Exit")

while True:
    user_message = input("\nYou: ")
    if user_message.lower() in ["bye", "exit", "15"]:
        print("Chatbot: Goodbye! Thank you for choosing Blink-IT.")
        break
    response = chatbot_response(user_message)
    print("Chatbot:", response)
