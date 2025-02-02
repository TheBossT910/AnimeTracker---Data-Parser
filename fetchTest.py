# Description: Fetches the next airing episode of an anime from AniList API
import requests
import datetime

from firebaseTest import AnimeFirebaseData

# getting anime name from Firebase
myObj = AnimeFirebaseData()
# get anime data
# Oshi no Ko: 6KaHVRxICvkkrRYsDiMY
# Spy x Family: OZtFGA9sVtdxtOCZZTEw
# Demon Slayer: Zn2VVQJZ8btUIsB3tDvb
myAnilistID = myObj.getAnime("Zn2VVQJZ8btUIsB3tDvb")
print(myAnilistID)  # prints the title of the anime

# AniList API Docs
# https://docs.anilist.co/

query = '''
query ($id: Int) {
  Media(id: $id, type: ANIME) {
    id
    bannerImage
    description
    title {
      romaji
      english
    }
    nextAiringEpisode {
      airingAt
      episode
    }
    coverImage {
      extraLarge
      large
      medium
    }
  }
}
'''

# Define our query variables and values that will be used in the query request
variables = {
    'id': myAnilistID
}

url = 'https://graphql.anilist.co'

# Make the HTTP Api request
response = requests.post(url, json={'query': query, 'variables': variables})

#  print the response
# print(response.json())

# display the image URLs
try:
  print(response.json()['data']['Media']['bannerImage'])
  print(response.json()['data']['Media']['coverImage']['extraLarge'])
  
except:
  print("No image found")

# displays the description
try:
  print(response.json()['data']['Media']['description']) 
except:
  print("No description found")

# print(response.json()['data']['Media']['coverImage']['large'])
# print(response.json()['data']['Media']['coverImage']['medium'])

# Extract the timestamp from the response
# timestamp = response.json()['data']['Media']['nextAiringEpisode']['airingAt']
# date = datetime.datetime.fromtimestamp(timestamp)  # Convert the timestamp to readable format
# print(date.strftime('%Y-%m-%d %H:%M:%S UTC'))  # Convert to readable format