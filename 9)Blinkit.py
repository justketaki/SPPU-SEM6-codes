import re

def blinkit_chatbot(user_input):
    user_input = user_input.lower()

    # Static electronics list to show if user says 'yes'
    electronics_list = """
Here are some electronics available:
- TV (Sony, Samsung, LG)
- Air Conditioner (Voltas, LG, Daikin)
- Bluetooth Headphones (boAt, JBL, Sony)
- Earphones (Wired/Wireless)
- Mobile Chargers (Fast charging, 65W, 30W)
- Power Banks (Realme, MI)
- Smartwatches (Apple, Noise, boAt)
- Laptops (Dell, HP, Lenovo)
- Tablets (Samsung, Lenovo)
- Speakers (JBL, boAt, Sony)
- Cameras (Canon, Nikon)
"""

    responses = {
        r"\b(hello|hi|hey)\b": "Hello! Welcome to Blinkit. What can I help you with today?",
        r"\b(order|buy|purchase)\b": "Great! Are you looking for groceries, electronics, premium products, or daily essentials?",
        r"\b(grocery|groceries)\b": "We offer fresh veggies, fruits, dairy, snacks, household items, and more. What do you need?",
        r"\b(5 min|5-minute delivery|fast delivery)\b": "We deliver essentials like milk, bread, fruits, and snacks in 5 minutes! ",
        r"\b(pencil|pen|notebook|stationery|eraser|sharpener|marker|highlighter|glue stick)\b": "Stationery items are available. Which ones do you want to add?",
        r"\b(potato|onion|bread|cheese|milk|butter|tomato|carrot|apple|banana|rice|wheat flour|sugar|salt|oil|paneer|curd)\b": "These grocery items are in stock.",
        r"\b(snacks|chips|biscuits|cookies|namkeen|popcorn)\b": "Snacks available!",
        r"\b(chocolates|candies|choco bars|dark chocolate|milk chocolate)\b": "We have a wide variety of chocolates: Cadbury, Ferrero Rocher, Lindt, Hershey's. Any favorites?",
        r"\b(sodas|cold drinks|soft drinks|energy drinks)\b": "We have sodas like Coke, Pepsi, Sprite, Red Bull, Monster Energy",
        r"\b(imported items|imported snacks|imported chocolates|imported sodas)\b": "Imported products available: Lindt Chocolates, Monster Drinks, Pringles, Doritos.",
        r"\b(premium products|luxury items|high end)\b": "We offer premium products like organic groceries, gourmet chocolates, luxury skincare, and imported goods. Interested?",
        r"\b(daily essentials|cleaning items|soap|shampoo|toothpaste|detergent|dishwasher|handwash|floor cleaner)\b": "Daily essentials and cleaning products are ready for quick delivery",
        r"\b(electronics|gadgets|tv|television|ac|air conditioner|bluetooth headphones|headphones|earphones|mobile charger|power bank|smartwatch|laptop|tablet|speaker|camera)\b": "Electronics available with warranty and fast delivery. Would you like to see options? (yes/no)",
        r"\b(add to cart|add item|add)\b": "Item added to your cart! Continue shopping or type 'checkout' to place your order.",
        r"\b(checkout|place order|confirm order)\b": "Your order has been placed successfully. You’ll get a confirmation shortly!",
        r"\b(track order|order status|where is my order)\b": "Track your order live via the Blinkit app under 'My Orders'.",
        r"\b(cancel order|order cancellation)\b": "To cancel an order, visit 'My Orders' section. ",
        r"\b(payment options|how to pay|payment methods)\b": "We accept UPI, credit/debit cards, net banking, and cash on delivery.",
        r"\b(customer support|help|talk to agent)\b": "Contact Blinkit support anytime at 1800-111-2222 or through our app Help Center.",
        r"\b(offers|discounts|promo code)\b": "Special offer: Use code 'BLINK20' for 20% off your first order!",
        r"\b(return policy|refund policy)\b": "You can return eligible items within 24 hours of delivery. Full refund on damaged products.",
        r"\b(thank you|thanks)\b": "You're welcome! Happy to help. Anything else you need?",
        r"\b(bye|exit)\b": "Goodbye! Thanks for shopping with Blinkit. Have a great day!"
    }

    # Track if last question asked was about electronics
    global last_question
    if user_input in ["yes", "yeah", "yup", "sure"]:
        if last_question == "electronics_options":
            last_question = None
            return electronics_list
        else:
            return "Can you please specify what you are saying 'yes' to?"
    elif user_input in ["no", "nah", "nope"]:
        if last_question == "electronics_options":
            last_question = None
            return "No problem! Let me know if you need help with anything else."
        else:
            return "Okay, let me know if you need anything else!"

    for pattern, response in responses.items():
        if re.search(pattern, user_input):
            if "electronics available with warranty" in response.lower():
                last_question = "electronics_options"
            else:
                last_question = None
            return response

    return "I'm sorry, I didn't catch that. Can you please rephrase or ask about a specific category?"

last_question = None

print("Welcome to Blinkit Customer Support! Type 'exit' to end the conversation.")

while True:
    user_message = input("You: ")
    if user_message.lower() in ["bye", "exit"]:
        print("Chatbot: Goodbye! Thanks for shopping with Blinkit!")
        break
    response = blinkit_chatbot(user_message)
    print("Chatbot:", response)

