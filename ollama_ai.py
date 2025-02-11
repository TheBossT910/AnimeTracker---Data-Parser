# Taha Rashid
# February 10 2025
# Using Ollama to run local AI models
# You need to start the Ollama app before we can run the program

from ollama import chat
from ollama import ChatResponse
from ai_prompts import Prompts

response: ChatResponse = chat(model='mistral', messages=[
  {
    'role': 'system',
    'content': Prompts.setup_prompt,
  },
  {
    'role': 'user',
    'content': Prompts.example_solo_leveling,
  },
])

print(response['message']['content'])
# or access fields directly from the response object
# print(response.message.content)
