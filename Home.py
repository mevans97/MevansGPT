import streamlit as st
import openai

#CHAT GPT FUNCTION TO CHAT AS WELL AS OPEN AI KEY

openai.api_key = "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"

def chat_with_mevans(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role":"user", "content": prompt}]
    )

    return response.choices[0].message.content.strip()

Chat_History = []

st.title("Mevans GPT") #This is the title for the webapp placed at the top of the screen

text = st.text_input("Enter some text 👇") #This is the prompt for the user to enter some text


Chat_History.append(text)

response = chat_with_mevans(text) #This utilizes the chat_with_mevans function I created in mevans.py

Chat_History.append(response)

for i in Chat_History:
    if Chat_History.index(i) % 2 == 1:
        st.text("Chatbot: ") #this displays the response from the function
        st.text(i)
    else:
        st.text("You: ")
        st.text(i)
