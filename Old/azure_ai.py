# Taha Rashid
# Febuary 9, 2025
# Testing out OpenAI on Azure



import os  
import base64
from openai import AzureOpenAI  
from credentials import Credentials

endpoint = os.getenv("ENDPOINT_URL", Credentials.azure_endpoint_url)  
deployment = os.getenv("DEPLOYMENT_NAME", "DeepSeek-R1")  
subscription_key = os.getenv("AZURE_OPENAI_API_KEY", Credentials.azure_open_ai_key)  

# Initialize Azure OpenAI Service client with key-based authentication    
client = AzureOpenAI(  
    azure_endpoint=endpoint,  
    api_key=subscription_key,  
    api_version="2024-05-01-preview",
)
    
    

#Prepare the chat prompt 
chat_prompt = [
    {
        "role": "system",
        "content": "AI prompt for Azure models:\nYou are an AI assistant specializing in generating episode recaps for my Anime Tracker app. Your goal is to create a natural, easy-to-read summary of the story up to the given episode, ensuring accuracy and coherence.\n\nInstructions:\n• Summarize all previous episodes up to the specified episode into a single flowing recap.\n• Base your recap strictly on the provided episode descriptions—do not invent or infer any new information.\n• Maintain a natural storytelling style, ensuring smooth transitions between key developments.\n• Keep the summary engaging but concise, capturing the essence of the story without excessive detail.\n• Maintain consistency with character names, events, and terminology used in the provided episode descriptions.\n• Do not include spoilers beyond the specified episode.\n\nInput Format:\n• Anime title: [Anime Name]\n• Episode number: [Current Episode Number]\n• Episode descriptions: [List of episode summaries]\n\nOutput Format:\n• A natural, flowing recap that reads like an organic summary of the anime’s progression.\n• No bullet points or list format, unless requested.\n• No assumptions or additional details beyond what is provided.\n\nExample Input:\n• Anime: \"Attack on Titan\"\n• Episode Number: 5\n• Episode Descriptions:\n○ Ep 1: Humanity lives inside walls to protect against Titans. Eren witnesses the fall of Wall Maria.\n○ Ep 2: Eren enlists in the military with Mikasa and Armin.\n○ Ep 3: The recruits undergo training.\n○ Ep 4: Titans breach Wall Rose. Eren leads the fight.\n○ Ep 5: (latest) Eren charges at a Titan but is seemingly devoured.\n\nExample Output:\nAs humanity struggles to survive behind massive walls, young Eren Yeager dreams of freedom beyond them. His world is shattered when Titans breach Wall Maria, forcing him and his friends Mikasa and Armin to seek refuge. Determined to fight back, they enlist in the military and undergo intense training, forming bonds with fellow recruits. But their hopes for a better future are short-lived—when Titans breach Wall Rose, chaos ensues. Eren leads the charge against the monstrous invaders, only to face a horrifying fate as he is swallowed by a Titan, leaving his friends in shock and despair."
    },
    {
        "role": "user",
        "content": "Anime: Solo Leveling Season 1\nEpisode Number: 4\nEpisode Descriptions:\nEpisode 1: Around ten years ago, gates that connected our world to another dimension began to appear, leading to the rise of hunters who would traverse these gates to fight the magic beasts within. Sung Jinwoo, E-Rank hunter, is the weakest of them all.\nEpisode 2: Jinwoo and his party appear to have cleared a low-level dungeon, when a hidden path to an unfamiliar temple is revealed. There they encounter a set of commandments and a group of monsters that cause them absolute despair.\nEpisode 3 (latest):  Jinwoo remains behind in the temple dungeon to save his few surviving party members, and with a swing from the god statue's blade, his life comes to an end—or so it seems, before he wakes up in a hospital bed."
    },
    # A previous response
    # {
    #     "role": "assistant",
    #     "content": "<think>\nOkay, let's tackle this. The user wants a recap of Solo Leveling up to episode 4. First, I need to go through each episode description provided and make sure I include all key points without adding anything extra. \n\nStarting with Episode 1: It sets up the world where gates appeared ten years ago, leading to hunters like Sung Jinwoo, who's an E-Rank, the weakest. That's the foundation.\n\nEpisode 2: Jinwoo's party clears a dungeon, finds a hidden path to a temple with commandments and monsters causing despair. Important to mention the hidden path and the despair they face here.\n\nEpisode 3: Jinwoo stays behind to save surviving members, gets killed by the statue's blade, but then wakes up in a hospital. The cliffhanger here is crucial—his apparent death and mysterious revival.\n\nNow, the challenge is to weave these points into a flowing narrative. Need to connect the episodes smoothly. Start with the setup of the gates and Jinwoo's status. Then move to the temple discovery, the danger they face, and Jinwoo's sacrifice. Finally, the twist of his survival. Make sure not to mention anything beyond episode 3. Keep it concise but engaging. Check that all key terms are consistent—like \"hunters,\" \"E-Rank,\" \"temple dungeon,\" etc. Avoid any bullet points, just a natural summary. Double-check that there are no added details beyond the provided episodes. Make sure the transition from his death to waking up in the hospital is clear but leaves the mystery intact as per the episode's end.\n</think>\n\nIn a world transformed by mysterious dimensional gates teeming with deadly magic beasts, Sung Jinwoo struggles to survive as humanity's weakest E-Rank hunter. While initially appearing to clear a routine low-level dungeon with his party, their discovery of a hidden temple unleashes unimaginable horror. Ancient commandments materialize as monstrous guardians slaughter most of the group, leaving Jinwoo to make a desperate last stand. Sacrificing himself to buy time for the few survivors, he's seemingly killed by a colossal blade from the temple's god statue - only to inexplicably awaken hours later in a hospital bed, his body unharmed but his reality forever altered by this brush with death."
    # }
] 
    
# Include speech result if speech is enabled  
messages = chat_prompt  
    
# Generate the completion  
completion = client.chat.completions.create(  
    model=deployment,
    messages=messages,
    max_tokens=800,  
    temperature=0.7,  
    top_p=0.95,  
    frequency_penalty=0,  
    presence_penalty=0,
    stop=None,  
    stream=False
)

print(completion.to_json())  
    