import nltk
from nltk.chat.util import Chat, reflections

# Pairs is a list of patterns and responses.
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today ?",]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there",]
    ],
    [
        r"what is your name ?",
        ["I am a chatbot created by you. You can call me Chatbot.",]
    ],
    [
        r"how are you ?",
        ["I'm doing good\nHow about You ?",]
    ],
    [
        r"sorry (.*)",
        ["Its alright","Its OK, never mind",]
    ],
    [
        r"i'm (.*) doing good",
        ["Nice to hear that","Alright :)",]
    ],
    [
        # quit word is used to exit the chat
        r"quit",
        ["Bye for now. See you soon :) ","It was nice talking to you. See you soon :)"]
    ],
]

def chatbot():
    print("Hi, I'm the chatbot you built") #default message at the start
    # initialising the chat object with pairs and reflections
    chat = Chat(pairs, reflections)
    # starting the conversation with the chatbot
    chat.converse()

if __name__ == "__main__":
    chatbot()