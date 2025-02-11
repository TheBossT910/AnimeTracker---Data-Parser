# Taha Rashid
# February 10 2025
# Using Ollama to run local AI models
# You need to start the Ollama app before we can run the program

from ollama import chat
from ollama import ChatResponse

response: ChatResponse = chat(model='mistral', messages=[
  {
    'role': 'user',
    'content': 'What is 1 + 2',
  },
])
print(response['message']['content'])
# or access fields directly from the response object
# print(response.message.content)
