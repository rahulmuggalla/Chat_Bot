from nltk.chat.util import Chat, reflections

reflections = {
  "i am"       : "you are",
  "i was"      : "you were",
  "i"          : "you",
  "i'm"        : "you are",
  "i'd"        : "you would",
  "i've"       : "you have",
  "i'll"       : "you'll",
  "my"         : "your",
  "you are"    : "I am",
  "you were"   : "I was",
  "you've"     : "I have",
  "you'll"     : "I'll",
  "your"       : "my",
  "yours"      : "mine",
  "you"        : "me",
  "me"         : "you"
}

#Pairs is a list of patterns and responses.
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today ?",]
    ],
    [
        r"(.*)(help)(.*) ",
        ["I can help you ",]
    ],
     [
        r"(.*) your name ?",
        ["My name is Bot, but you can just call me robot and I'm a chatbot .",]
    ],
    [
        r"(.*)(how are you)(.*) ?",
        ["I'm doing very well", "i am great !"]
    ],
    [
        r"(.*)(sorry)(.*)",
        ["Its alright","Its OK, never mind that",]
    ],
    [
        r"i'm (.*) (good|well|okay|ok)",
        ["Nice to hear that","Alright, great !",]
    ],
    [
        r"(hi|hey|hello|hola|holla)(.*)",
        ["Hello", "Hey there",]
    ],
    [
        r"what (.*) want ?",
        ["Make me an offer I can't refuse",]
        
    ],
    [
        r"(.*)created(.*)",
        ["Muggalla Rahul created me using Python's NLTK library ","top secret ;)",]
    ],
    [
        r"(.*) (location|city) ?",
        ['Vijayawada, India',]
    ],
    [
        r"how is weather in (.*)?",
        ["Weather in %1 is awesome like always","Too hot man here in %1","Too cold man here in %1","Never even heard about %1"]
    ],
    [
        r"(.*)raining in (.*)",
        ["No rain in the past 4 days here in %2","In %2 there is a 50% chance of rain",]
    ],
    [
        r"how (.*) health (.*)",
        ["Health is very important, but I am a computer, so I don't need to worry about my health ",]
    ],
    [
        r"(.*)(sports|game|sport)(.*)",
        ["I'm a very big fan of Tennis",]
    ],
    [
        r"who (.*) sportsperson ?",
        ["Roger Federer", "Virat Kohli"]
    ],
    [
        r"who (.*) (moviestar|actor)?",
        ["Prabhas", "Krithik Roshan"]
    ],
    [
        r"quit",
        ["Bye for now. See you soon :) ","It was nice talking to you. See you soon :)"]
    ],
    [
        r"(.*)",
        ['That is nice to hear']
    ],
]


#default message at the start of chat
print("Hi, I'm bot created by Rahul and I like to chat\nPlease type lowercase English language to start a conversation. Type quit to leave ")

#Create Chat Bot
chat = Chat(pairs, reflections)

#Start conversation
chat.converse()