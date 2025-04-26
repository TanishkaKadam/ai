# Define the dictionary with sample customer queries as keys and bot responses as values
response_dict = {
    "hello": "Hi! Welcome to our customer support. How can I assist you today?",
    "hi": "Hello! How can I help you today?",
    "how are you": "I'm just a bot, but I'm happy to assist you!",
    "what is your name": "I'm your helpful customer support bot. No name, just here to help!",
    "goodbye": "Goodbye! Have a wonderful day!",
    "help": "You can ask me about our services, products, or our office hours.",
    "services": "We offer customer support, product information, order tracking, and much more.",
    "hours": "Our office hours are from 9 AM to 5 PM, Monday through Friday.",
    "order status": "Please provide your order ID to check the status of your order.",
    "payment methods": "We accept credit cards, debit cards, and PayPal.",
    "return policy": "You can return items within 30 days of purchase for a full refund.",
    "shipping": "We offer free standard shipping on orders over $50.",
    "contact": "You can reach us at support@ourcompany.com or call us at 123-456-7890."
}

# Function to handle customer interaction
def chatbot():
    print("Hello, welcome to our customer service chatbot! Type 'goodbye' to exit.")
    while True:
        # Get user input (customer's query)
        user_input = input("You: ").lower().strip()  # Convert to lowercase for consistency

        # Check if the input matches a key in the response dictionary
        if user_input in response_dict:
            print(f"Bot: {response_dict[user_input]}")
        else:
            print("Bot: Sorry, I didn't understand that. Can you please ask something else?")

        # Exit condition
        if user_input == "goodbye":
            break

# Run the chatbot
chatbot()
