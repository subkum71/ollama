# Basis of Agentic AI, How LLM Call the Tool
# Defining function which LLM will call to Answer your query
# Function1 : Function for City Temparature
# Function2 : Origin City for given Fruits 
'''Tool definition given to Ollama
tools = [
    {
        "type": "function",
        "function": {
            "name": "Get_FruitOrigin",
            "description": "Get the origin regions/cities of a fruit",
            "parameters": {
                "type": "object",
                "properties": {
                    "fruit": {
                        "type": "string",
                        "description": "Name of the fruit"
                    }
                },
                "required": ["fruit"]
            }
        }
    }
]
But if you use langchain(ChatOllama) no need definitions only need to pass tool
Your current flow
User Query
    ↓
ChatOllama (LLM)
    ↓
Decides which tool to call
    ↓
Get_FruitOrigin() OR Get_Temp()
    ↓
Tool Result
Optional
   Submit Result to LLM to get final response 
'''
import ollama
from langchain_ollama import ChatOllama
from langchain_core.messages import ToolMessage

#Common Paramters
Model_name="qwen3-vl:4b"
llm_with_tools=""

# Get the City Temp
def Get_Temp(city) -> str:
    temperatures = {
        "Delhi": "30°C",
        "Mumbai": "28°C",
        "Bangalore": "24°C",
        "Chennai": "32°C"
    }
    return f"The temperature in {city} is {temperatures.get(city, 'Not available')}"

# Get the Origin of the Fruit 
def Get_FruitOrigin(fruit) -> str:
    fruits = {
        "Apple": ["Kashmir", "Himachal Pradesh"],
        "Mango": ["Uttar Pradesh", "Maharashtra", "Andhra Pradesh"],
        "Orange": ["Nagpur", "Punjab", "Assam"],
        "Banana": ["Tamil Nadu", "Maharashtra", "Gujarat"],
        "Grapes": ["Nashik", "Karnataka", "Andhra Pradesh"]
    }
    return f"{fruit} originates from: {', '.join(fruits.get(fruit, ['Unknown']))}"

#------------------------Main -----------------------------------------
llm = ChatOllama(
        model= Model_name,
        temperature=0
)

# -----------------------------
# Bind tools to LLM
# -----------------------------
llm_with_tools = llm.bind_tools([
        Get_FruitOrigin,
        Get_Temp
])

def Call_LLM_Tools(question):
    print("Please wait processing your request ...")
## 1. Ask LLM which tool it wants
    answer = llm_with_tools.invoke(question)

## Optional:  # 2. Store original response + tool results
    messages = [answer]
## 3. Now need to call the Tool
##Execute the requested tool
    for tool_call in answer.tool_calls:
        
        if tool_call["name"] == "Get_Temp":
            result = Get_Temp(**tool_call["args"])
            print("Tool Answer :", result)
        elif tool_call["name"] == "Get_FruitOrigin":
            result = Get_FruitOrigin(**tool_call["args"])
            print("Tool Answerb:", result)
        else:
         print ("My Answer : Out of my scope:Not able to answer")
## Here result store the result from Tool not from LLM
## This Can be given to user as response or send it back to LLM to give final response
# 3. Add tool result -Optional
    messages.append(
        ToolMessage(
                content=str(result),
                tool_call_id=tool_call["id"]
                    )
        )
#4. Send tool result back to LLM --Optional
    final_answer = llm_with_tools.invoke(messages)
    print ("Please wait for LLM final response ...")
    print("LLM Response:",final_answer.content)

print("Enter your question, Limited to City Temp or Fruits Origin City !! ")
while True:
    question = input("\nYou: ")
    if question.lower() == "exit":
        break
    Call_LLM_Tools(question)
        

        
