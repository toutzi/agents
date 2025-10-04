# Start with imports - ask ChatGPT to explain any package that you don't know
import os
import json
from dotenv import load_dotenv
from openai import OpenAI
from anthropic import Anthropic
from IPython.display import Markdown, display

# Load environment variables from a .env file
# The .env file should contain your API keys
load_dotenv(override=True)

# Print the key prefixes to help with any debugging
openai_api_key = os.getenv('OPENAI_API_KEY')
anthropic_api_key = os.getenv('ANTHROPIC_API_KEY')
google_api_key = os.getenv('GOOGLE_API_KEY')
deepseek_api_key = os.getenv('DEEPSEEK_API_KEY')
groq_api_key = os.getenv('GROQ_API_KEY')


if openai_api_key:
   print(f"OpenAI API Key exists and begins {openai_api_key[:8]}")
else:
   print("OpenAI API Key not set")
  
if anthropic_api_key:
   print(f"Anthropic API Key exists and begins {anthropic_api_key[:7]}")
else:
   print("Anthropic API Key not set (and this is optional)")


if google_api_key:
   print(f"Google API Key exists and begins {google_api_key[:2]}")
else:
   print("Google API Key not set (and this is optional)")


if deepseek_api_key:
   print(f"DeepSeek API Key exists and begins {deepseek_api_key[:3]}")
else:
   print("DeepSeek API Key not set (and this is optional)")


if groq_api_key:
   print(f"Groq API Key exists and begins {groq_api_key[:4]}")
else:
   print("Groq API Key not set (and this is optional)")


# Generate a scenario
request = "Please come up with a challenging, nuanced question that I can ask a number of LLMs to evaluate their intelligence. "
request += "Answer only with the question, no explanation."
messages = [{"role": "user", "content": request}]


openai = OpenAI()
response = openai.chat.completions.create(
   model="gpt-4o-mini",
   messages=messages,
)
question = response.choices[0].message.content
print(question)


# Store competitors and answers
competitors = []
answers = []
messages = [{"role": "user", "content": question}]


# Competitor #1: GPT
model_name = "gpt-4o-mini"


response = openai.chat.completions.create(model=model_name, messages=messages)
answer = response.choices[0].message.content


display(Markdown(answer))
competitors.append(model_name)
answers.append(answer)


# Competitor #2: Deepseek
deepseek = OpenAI(api_key=deepseek_api_key, base_url="https://api.deepseek.com/v1")
model_name = "deepseek-chat"


response = deepseek.chat.completions.create(model=model_name, messages=messages)
answer = response.choices[0].message.content


display(Markdown(answer))
competitors.append(model_name)
answers.append(answer)


# Competitor #3: locally installed llama3
ollama = OpenAI(base_url='http://localhost:11434/v1', api_key='ollama')
model_name = "llama3"


response = ollama.chat.completions.create(model=model_name, messages=messages)
answer = response.choices[0].message.content


display(Markdown(answer))
competitors.append(model_name)
answers.append(answer)




# Competitor not consulted
# ------------------------
# Anthropic has a slightly different API, and Max Tokens is required
""" 
model_name = "claude-3-7-sonnet-latest"


claude = Anthropic()
response = claude.messages.create(model=model_name, messages=messages, max_tokens=1000)
answer = response.content[0].text


display(Markdown(answer))
competitors.append(model_name)
answers.append(answer)


# Gemini
gemini = OpenAI(api_key=google_api_key, base_url="https://generativelanguage.googleapis.com/v1beta/openai/")
model_name = "gemini-2.0-flash"


response = gemini.chat.completions.create(model=model_name, messages=messages)
answer = response.choices[0].message.content


display(Markdown(answer))
competitors.append(model_name)
answers.append(answer)


# Groq llama
groq = OpenAI(api_key=groq_api_key, base_url="https://api.groq.com/openai/v1")
model_name = "llama-3.3-70b-versatile"


response = groq.chat.completions.create(model=model_name, messages=messages)
answer = response.choices[0].message.content


display(Markdown(answer))
competitors.append(model_name)
answers.append(answer)
"""
# ------------------------




# print answers
display(Markdown(answer))
competitors.append(model_name)
answers.append(answer)

print(competitors)
print(answers)


# It's nice to know how to use "zip"
for competitor, answer in zip(competitors, answers):
   print(f"Competitor: {competitor}\n\n{answer}")


# Let's bring this together - note the use of "enumerate"
together = ""
for index, answer in enumerate(answers):
   together += f"# Response from competitor {index+1}\n\n"
   together += answer + "\n\n"
print(together)


# Let's create a judge to evaluate the best model
judge = f"""You are judging a competition between {len(competitors)} competitors.
Each model has been given this question:


{question}


Your job is to evaluate each response for clarity and strength of argument, and rank them in order of best to worst.
Respond with JSON, and only JSON, with the following format:
{{"results": ["best competitor number", "second best competitor number", "third best competitor number", ...]}}

Here are the responses from each competitor:

{together}


Now respond with the JSON with the ranked order of the competitors, nothing else. Do not include markdown formatting or code blocks."""
print(judge)




judge_messages = [{"role": "user", "content": judge}]


openai = OpenAI()
response = openai.chat.completions.create(
   model="o3-mini",
   messages=judge_messages,
)
results = response.choices[0].message.content
print(results)


# OK let's turn this into results!
results_dict = json.loads(results)
ranks = results_dict["results"]
for index, result in enumerate(ranks):
   competitor = competitors[int(result)-1]
   print(f"Rank {index+1}: {competitor}")


# the output looks like this:
# Rank 1: deepseek-chat
# Rank 2: gpt-4o-mini
# Rank 3: llama3
