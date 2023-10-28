import openai

openai.api_key = "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"

def chat_with_mevans(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role":"user", "content": prompt}]
    )

    return response.choices[0].message.content.strip()

if __name__=="__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower in ["quit", "exit", "bye"]:
            break

        response = chat_with_mevans(user_input)
        print("Chatbot: ", response)