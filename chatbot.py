import re

def simple_chatbot(user_input):
    

    user_input = user_input.lower()  

    
    if re.search(r"\b(hello|hi|hey|greetings)\b", user_input):
        return "Hello! How can I help you today?"

    
    elif re.search(r"\b(bye|goodbye|see you|later)\b", user_input):
        return "Goodbye! Have a great day."

    
    elif re.search(r"\b(what are you|who are you|what is your name)\b", user_input):
         return "I am a simple chatbot built to demonstrate basic conversation flow."

    elif re.search(r"\b(how are you|how's it going)\b", user_input):
        return "I'm doing well, thank you for asking!"

    
    elif re.search(r"\b(weather|temperature)\b", user_input):
        return "I'm not equipped to provide real-time weather information. Try searching online."

    
    elif re.search(r"\b(help|assistance)\b", user_input):
        return "I can respond to simple greetings, farewells, and questions about myself. Try saying 'hello' or 'goodbye'."

    
    else:
        return "I'm not sure I understand. Could you please rephrase your question?"



print("Welcome to the Simple Chatbot!")
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Chatbot: Goodbye!")
        break
    response = simple_chatbot(user_input)
    print("Chatbot:", response)
