from util import match_intent , get_response


def chatbot():
    print("Rule base chatbot")
    print("Type 'bye' to exit.\n")
    
    while True:
        user_input = input("You: ").strip().lower()
        
        intent_list = match_intent(user_input)
        
        if intent_list:
            response = get_response(intent_list)
            print(f"Chatbot: {response}\n")
            
            if intent_list == "goodbye":
                break
        else:
            print("Chatbot: I don't understand that.\n")
            
if __name__ == "__main__":
    chatbot()