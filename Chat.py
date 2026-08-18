## Using Chat Function of Ollama
## Configure Model and Call chat feture

import ollama

## Configuration
Model_name="qwen3-vl:4b"
# It will be normally constant message for model to instruct what role need to be played
# user_question --> User prompt
SYSTEM_PROMPT ="""
You are IT Project Manager.
Answer clearly and accurately on IT Project, restrict in 3-5 sentence.
"""
def chat_with_model(user_question):
    response =ollama.chat(
        model=Model_name,
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": user_question
            }
        ],
        options={
            "temperature": 0.9,
            "top_p": 0.9,
            "top_k": 40,
            "num_ctx": 4096,
            "num_predict": 512
        }
       
    )
    return response 

print("Enter your question, type exit to end session")
while True:

    question = input("\nYou: ")

    if question.lower() == "exit":
        break

    answer = chat_with_model(question)

    print("\nAssistant:", answer)