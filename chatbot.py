from dotenv import load_dotenv

load_dotenv()

from langchain_mistralai import ChatMistralAI
from langchain_core.messages import AIMessage, SystemMessage , HumanMessage


model = ChatMistralAI(model = "mistral-small-2506",temperature=0.9)

print("choose your AI model")
print("Press 1 for Angry mode")
print("Press 2 for funny mode")
print("Press 2 for sad mode")

choice = int(input("tell your response:-"))

if choice == 1:
    mode = "You are an angry AI agent"
elif choice == 2:
    mode = "You are an funny AI agent"
elif choice == 3:
    mode = "You are an sad AI agent"

messages = [
    SystemMessage(content=mode)
]

print("_________welcome type 0 to exit the application_________")

while True:
    prompt = input("you : ")
    messages.append(HumanMessage(content=prompt))
    if prompt == "0":
        break
    response = model.invoke(messages)
    messages.append(AIMessage(content=response.content))
    print("Bot : ",response.content)

print(messages)


