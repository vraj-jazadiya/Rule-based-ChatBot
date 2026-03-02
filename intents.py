import re
import random

intents = {
    "greeting":{
        "patterns":[r"\bhello\b",r"\bhi\b",r"\bhey\b" , r"\bhy\b"],
        "responses":["Hello there!" , "Hi, How are you" , "Hey, Nice to meet you~~!"]
    },
    "time": {
        "patterns": [r"what.*time", r"current time", r"tell me the time"],
        "responses": []
    },
    "date": {
        "patterns": [r"what.*date", r"today.*date", r"current date"],
        "responses": []
    },

    "goodbye": {
        "patterns": [r"\bbye\b", r"goodbye" , r"exit"],
        "responses": ["Goodbye! 👋","See you later!"]
    }
}
