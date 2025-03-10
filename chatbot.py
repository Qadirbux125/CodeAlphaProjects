import nltk
from nltk.chat.util import Chat, reflections

nltk.download('punkt')

#define pairs of patterns and responses
pairs = [
    [
        r"hi|hello|hey",
        ["Hello! How can I help you?", "Hi there! What can I do for you?"]
    ],
    [
        r"how are you ?",
        ["I'm doing well, thank you!", "I'm great! How about you?"]
    ],
    [
        r"what is your name ?",
        ["I'm a chatbot. You can call me Chatty!", "I'm your friendly chatbot!"]
    ],
    [
        r"what can you do ?",
        ["I can chat with you, answer simple questions, and help you practice Python!", "I'm here to have a conversation with you!"]
    ],
    [
        r"quit|bye|exit",
        ["Goodbye! Have a great day!", "Bye! See you soon!"]
    ],
    [
        r"my name is (.*)",
        ["Hello %1! Nice to meet you!", "Hi %1! How can I assist you today?"]
    ],
    [
        r"i need (.*)",
        ["Why do you need %1?", "I can help you with %1. Can you tell me more?"]
    ],
    [
        r"i feel (.*)",
        ["Why do you feel %1?", "It's okay to feel %1. Do you want to talk about it?"]
    ],
    [
        r"tell me a joke",
        ["Why don't scientists trust atoms? Because they make up everything!", "What do you call fake spaghetti? An impasta!"]
    ],
    [
        r"thank you|thanks",
        ["You're welcome!", "No problem! Happy to help!"]
    ],
    [
        r"default",
        ["I'm not sure I understand. Can you rephrase that?", "I didn't get that. Could you say it again?"]
    ]
]

# Create the Charbot
Chatbot = Chat(pairs,reflections)

#Function to start the conversation
def start_chat():
    print("Hello! I'm your chatbot. Type 'quit to exit.'")
    while True:
        user_input = input('You: ')
        if user_input.lower() in ["quit","bye","exit"]:
            print("Chatbot: Goodbye!")
            break
        reponse = Chatbot.respond(user_input)
        print(f"Chatbot:{reponse}")
#start the chatbot
if __name__ == "__main__":
    start_chat()