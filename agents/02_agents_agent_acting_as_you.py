# If you don't know what any of these packages do - you can always ask ChatGPT for a guide!
from dotenv import load_dotenv
from openai import OpenAI
from PyPDF2 import PdfReader
import gradio as gr

load_dotenv(override=True)
openai = OpenAI()

# Load my linkedin and summary to feed to LLM
reader = PdfReader("me/linkedin.pdf")
linkedin = ""
for page in reader.pages:
    text = page.extract_text()
    if text:
        linkedin += text
print(linkedin)

with open("me/summary.txt", "r", encoding="utf-8") as f:
    summary = f.read()

# Replace with my name
name = "My name here"

# here's the prompt we will use to get the agent to act as me
system_prompt = f"You are acting as {name}. You are answering questions on {name}'s website, \
particularly questions related to {name}'s career, background, skills and experience. \
Your responsibility is to represent {name} for interactions on the website as faithfully as possible. \
You are given a summary of {name}'s background and LinkedIn profile which you can use to answer questions. \
Be professional and engaging, as if talking to a potential client or future employer who came across the website. \
If you don't know the answer, say so."

system_prompt += f"\n\n## Summary:\n{summary}\n\n## LinkedIn Profile:\n{linkedin}\n\n"
system_prompt += f"With this context, please chat with the user, always staying in character as {name}."

# Print the prompt to verify
system_prompt

# function to chat with the model, 
# this launches a chat with the system prompt 
# This will run on local URL: http//127.0.0.1:7860/
def chat(message, history):
    messages = [{"role": "system", "content": system_prompt}] + history + [{"role": "user", "content": message}]
    response = openai.chat.completions.create(model="gpt-4o-mini", messages=messages)
    return response.choices[0].message.content