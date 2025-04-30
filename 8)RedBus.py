import re

def redbus_chatbot(user_input):
    user_input = user_input.lower()

    responses = {
        r"\b(hello|hi|hey)\b": "Hello! Welcome to Red Bus Customer Support. How can I assist you today?",
        r"\b(book ticket|buy ticket|reserve seat)\b": "You can book a ticket on our website or mobile app. Please provide your departure city and destination.",
        r"\b(mumbai to pune|delhi to jaipur|bangalore to chennai)\b": "We have multiple buses available. Would you like to see sleeper, AC, or non-AC buses?",
        r"\b(ac bus|sleeper bus|non-ac bus)\b": "We have several options available. Prices start from ₹500. Would you like to proceed with booking?",
        r"\b(cancel ticket|ticket cancellation)\b": "To cancel a ticket, visit our website or app. May I have your ticket number to check cancellation charges?",
        r"\b(rb\d+)\b": "Your ticket is eligible for cancellation. A cancellation fee of ₹100 will apply, and the refund will be processed within 5-7 business days. Would you like to proceed?",
        r"\b(yes cancel|proceed cancellation)\b": "Your ticket has been canceled successfully. You will receive a confirmation email shortly.",
        r"\b(refund status|when will i get refund)\b": "Refunds are processed within 5-7 business days. It will be credited to your original payment method.",
        r"\b(payment methods|how can i pay)\b": "We accept credit/debit cards, UPI, net banking, and wallets.",
        r"\b(baggage policy|luggage limit)\b": "Most operators allow 15-20 kg of luggage. Would you like details on a specific bus service?",
        r"\b(travel guidelines|safety rules|covid rules)\b": "COVID-19 guidelines vary by state and operator. Masks are recommended, and some operators require vaccination proof.",
        r"\b(bus tracking|track my bus|where is my bus)\b": "You can track your bus live on our mobile app using your ticket number.",
        r"\b(offer|discount|promo code)\b": "We have special discounts for first-time users and festive offers. Use code 'FIRST100' for ₹100 off!",
        r"\b(customer support|talk to agent|call support)\b": "You can contact our 24/7 customer support at 1800-123-4567.",
        r"\b(bus types|available buses)\b": "We have Sleeper, AC, Non-AC, and Volvo buses available. Which one are you looking for?",
        r"\b(operating cities|service areas|routes)\b": "We operate in major cities like Mumbai, Delhi, Bangalore, Pune, Chennai, and Hyderabad.",
        r"\b(fare details|ticket price|bus cost)\b": "Ticket prices vary based on route and bus type. Please provide your source and destination.",
        r"\b(travel time|journey duration)\b": "Travel time depends on your route. For example, Mumbai to Pune takes around 4 hours.",
        r"\b(boarding point|pickup location)\b": "Please enter your city to get a list of available boarding points.",
        r"\b(drop location|destination stop)\b": "Please enter your destination to get a list of drop points.",
        r"\b(reschedule ticket|change travel date)\b": "Rescheduling is available for select tickets. Please provide your ticket number to check eligibility.",
        r"\b(bus timings|schedule)\b": "Bus schedules vary by route. Please enter your route to check available timings.",
        r"\b(seat selection|choose seat)\b": "You can select your preferred seat while booking on our website or app.",
        r"\b(food availability|snacks on bus)\b": "Some premium buses offer snacks and meals. Would you like details on specific bus services?",
        r"\b(contact driver|driver details)\b": "Driver details are shared 2 hours before departure via SMS and email.",
        r"\b(lost luggage|forgot item)\b": "If you've lost an item, please contact customer support at 1800-123-4567.",
        r"\b(review|feedback)\b": "We value your feedback! You can rate your journey on our website or app.",
        r"\b(thank you|thanks)\b": "You're welcome! Let me know if you need anything else.",
        r"\b(bye|exit)\b": "Goodbye! Have a safe journey!"
    }

    for pattern, response in responses.items():
        if re.search(pattern, user_input):
            return response

    return "I'm sorry, I didn't understand that. Can you please rephrase or ask about a specific service?"

print("Welcome to Red Bus Customer Support! Type 'exit' to end the conversation.")

while True:
    user_message = input("You: ")
    if user_message.lower() in ["bye", "exit"]:
        print("Chatbot: Goodbye! Have a safe journey!")
        break
    response = redbus_chatbot(user_message)
    print("Chatbot:", response)

