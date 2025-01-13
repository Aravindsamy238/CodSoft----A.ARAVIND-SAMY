import re
import datetime

def chatbot():
    print("Hello! I'm a chatbot. Type 'exit' to end the conversation.")
    
    while True:
        user_input = input("You: ").lower().strip()
        
        if user_input == 'exit' or user_input == 'bye':
            print("Chatbot: Goodbye! Have a great day!")
            break
        
        elif re.search(r"hello|hi|hey", user_input):
            print("Chatbot: Namaste! How can I assist you today?")
        elif re.search(r"how are you", user_input):
            print("Chatbot: I'm doing well, thank you! How are you?")
        elif re.search(r"india", user_input):
            print("Chatbot: India is a beautiful country known for its rich history, culture, and diverse traditions!")
        elif re.search(r"what is your name", user_input):
            print("Chatbot: My name is Ramu!")
        elif re.search(r"what is the time", user_input):
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"Chatbot: The current time is {current_time}.")
        elif re.search(r"what is the date", user_input):
            current_date = datetime.datetime.now().strftime("%Y-%m-%d")
            print(f"Chatbot: Today's date is {current_date}.")
        else:
            print("Chatbot: I'm sorry, I didn't understand that. Can you please rephrase?")
chatbot()
