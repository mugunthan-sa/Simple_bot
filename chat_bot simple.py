import openai

# Replace with your actual API key
api_key = "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"

openai.api_key = api_key

def chat_with_gpt(prompt):
    response = openai.ChatCompletion.create(
        model= "gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
        
    )

    return response.choices[0].message.content.strip()
if __name__ == "__main":
    while True:
        user_input=input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            break 
        response = chat_with_gpt(user_input) 
        print("Chatbot: ", response)


        