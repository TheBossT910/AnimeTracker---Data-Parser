# Taha Rashid
# January 28, 2025
# Description: Fetches the next airing episode of an anime from AniList API

import requests
import datetime

from database import AnimeFirebaseData

# getting anime name from Firebase
myObj = AnimeFirebaseData()
# get anime data
# Oshi no Ko: 6KaHVRxICvkkrRYsDiMY
# Spy x Family: OZtFGA9sVtdxtOCZZTEw
# Demon Slayer: Zn2VVQJZ8btUIsB3tDvb
myAnilistID = myObj.getAnime("SAKAMOTO DAYS")
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
bannerImage = ""
coverImage = ""
try:
  bannerImage = response.json()['data']['Media']['bannerImage']
  coverImage = response.json()['data']['Media']['coverImage']['extraLarge']
  
  print(bannerImage)
  print(coverImage)
except:
  print("No image found")

# displays the description
description = ""
try:
  description = response.json()['data']['Media']['description']
  print(description) 
except:
  print("No description found")

# Extract the timestamp from the response
date = ""
try:
  timestamp = response.json()['data']['Media']['nextAiringEpisode']['airingAt'] 
  date = datetime.datetime.fromtimestamp(timestamp)  # Convert the timestamp to readable format
  date = date.strftime('%Y-%m-%d %H:%M:%S UTC')
  print(date)  # Convert to readable format
except:
  print("No airing date found")