# Define the dictionary with sample customer queries as keys and bot responses as values
cust_dict = {
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



def chatbot(user_input):
    if user_input in cust_dict:
        print(cust_dict[user_input])
    else:
        print("I'm sorry, I don't understand that.")

# Chat loop
while True:
    strt = input("Enter your Response: ")
    chatbot(strt)
   
    if strt == "Bye":
        break
