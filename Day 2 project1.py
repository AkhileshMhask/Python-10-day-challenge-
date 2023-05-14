'''import random as rd


greeting = ["jevli kay ","Good afternooon "," oyee "," paavn jevlaa ka  "," I love you"]
for i in range(len(greeting)):
   print(rd.choice(greeting))

greetings = ["How are you ?","What's up, %s?","bye bye %s"]

message= rd.choice(greetings) %('Akhilesh')

print(message)'''



import random

# define some responses
greetings = ["hello", "hi", "hey"]
goodbyes = ["bye", "goodbye", "see you later"]
thanks = ["thank you", "thanks", "much appreciated"]
unknown = ["I'm sorry, I didn't understand that.", "Could you please rephrase that?"]

# define the chatbot function
def chatbot():
    # greet the user
    print("Hi, I'm a chatbot. What can I help you with today?")

    # keep chatting until the user says goodbye
    while True:
        # get user input
        user_input = input().lower()

        # check for greetings
        if user_input in greetings:
            print("Hello there!")
        # check for goodbyes
        elif user_input in goodbyes:
            print("Goodbye!")
            break
        # check for thanks
        elif user_input in thanks:
            print("You're welcome!")
        # if the user says something unknown, respond with a random message from the unknown list
        else:
            print(random.choice(unknown))

# call the chatbot function to start the conversation
chatbot()
