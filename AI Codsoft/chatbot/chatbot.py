import re

def chatbot():
    print("Chatbot: Hi! I'm your assistant. Type 'bye' to exit.\n")
    
    while True:
        try:
            user_input = input("You: ").strip()
            
            if not user_input:
                continue
            
            user_lower = user_input.lower()
            
            if re.search(r'\b(bye|exit|quit|goodbye)\b', user_lower):
                print("Chatbot: Goodbye! Have a great day!\n")
                break
            elif re.search(r'\b(hi|hello|hey|greetings)\b', user_lower):
                print("Chatbot: Hello! How can I help you today?\n")
            elif re.search(r'\b(how are you|how do you do|whats up|wassup)\b', user_lower):
                print("Chatbot: I'm doing great, thanks for asking! How about you?\n")
            elif re.search(r'\b(your name|who are you|what are you)\b', user_lower):
                print("Chatbot: I'm a rule-based chatbot created to assist you!\n")
            elif re.search(r'\b(help|assist|what can you do|your capabilities)\b', user_lower):
                print("Chatbot: I can chat, answer questions, and help with basic conversations!\n")
            elif re.search(r'\b(thanks|thank you|thx|appreciate)\b', user_lower):
                print("Chatbot: You're very welcome! Happy to help!\n")
            elif re.search(r'\b(good|great|awesome|nice|excellent)\b', user_lower):
                print("Chatbot: That's wonderful to hear!\n")
            elif re.search(r'\b(bad|sad|terrible|awful|not good)\b', user_lower):
                print("Chatbot: I'm sorry to hear that. I hope things get better!\n")
            elif re.search(r'\b(weather|temperature|forecast)\b', user_lower):
                print("Chatbot: I can't check the weather, but I hope it's nice where you are!\n")
            elif re.search(r'\b(time|clock|hour)\b', user_lower):
                print("Chatbot: I don't have access to the current time, sorry!\n")
            elif re.search(r'\b(joke|funny|laugh)\b', user_lower):
                print("Chatbot: Why did the chatbot go to school? To improve its responses!\n")
            elif re.search(r'\b(age|old|birthday)\b', user_lower):
                print("Chatbot: I was just created, so I'm pretty new!\n")
            elif re.search(r'\b(love|like)\b.*\byou\b', user_lower):
                print("Chatbot: That's kind of you! I enjoy chatting with you too!\n")
            elif '?' in user_input:
                print("Chatbot: That's an interesting question! I'm still learning to answer more.\n")
            else:
                print("Chatbot: I see! Tell me more about that.\n")
                
        except KeyboardInterrupt:
            print("\n\nChatbot: Goodbye! Take care!\n")
            break
        except Exception as e:
            print(f"Chatbot: Oops, something went wrong. Let's continue!\n")

if __name__ == "__main__":
    chatbot()
