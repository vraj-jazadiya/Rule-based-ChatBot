import re 
import random
from datetime import datetime
from intents import intents

def match_intent(user_input):
    match_intents = []
    for intent_name , intents_data in intents.items():
        for pattern in intents_data["patterns"]:
            if re.search(pattern, user_input, re.IGNORECASE):
                match_intents.append(intent_name)
                break
    return match_intents            
            
   
def dynamic_response(intent_name):
    if intent_name == "time":
        now = datetime.now()
        return f"The current time is {now.strftime('%H:%M:%S')}"
    if intent_name == "date":
        now = datetime.now()
        return f"Today's date is {now.strftime('%Y-%m-%d')}" 
    
    return None

def get_response(intent_list):
    responses = []
    
    for intent_name in intent_list:
        dynamic = dynamic_response(intent_name)
        if dynamic: 
            responses.append(dynamic)
        else:    
            rdm_responses = random.choice(intents[intent_name]["responses"])
            responses.append(rdm_responses)
    return " | ".join(responses)