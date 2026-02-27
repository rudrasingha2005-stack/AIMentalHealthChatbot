from google.genai import  Client
from google.genai import types

#client = Client(api_key="AIzaSyDRSs0VO9tsYpQroM0LhpzMePEqTENEKoI")
client = Client(api_key="AIzaSyBG5ZDn9IyiORXZznuNxergvw7rXR_PsOw")
print("WELCOME TO MENTAL HEALTH SUPPORT")
print("I hope you are doing well today .Please tell me your thoughts(Type endchat to exit)")

userinput=input("user: ")
while userinput.lower()!= 'endchat':
    systemoutput=client.models.generate_content(
        contents= userinput,
        model= 'gemini-2.5-flash-lite',
        config= types.GenerateContentConfig(
            system_instruction="You are a mental health support agent.Answer in 1-10 line, within 2000 characters.Don't be over judgemental ,be little empathetic"
        )
    )
    print("Chatbot: "+systemoutput.text)
    userinput = input("user: ")