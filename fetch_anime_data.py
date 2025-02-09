# Taha Rashid
# Feburary 8, 2025
# Description: Fetches the data of an anime using the AniList API

import requests
import datetime

from firebaseTest import AnimeFirebaseData

# function to convert timestamp to readable date
def timeConverter(timestamp):
    date = ""
    try:
        date = datetime.datetime.fromtimestamp(timestamp)  # Convert the timestamp to readable format
        date = date.strftime('%Y-%m-%d %H:%M:%S UTC')
        return date
    except:
        return "No airing date found"

# AniList API Docs
# https://docs.anilist.co/

query = '''
query($mediaId: Int)  {
  Media(id: $mediaId) {
    title {
      romaji
      english
      native
    }
    episodes
    season
    seasonYear
    coverImage {
      extraLarge
    }
    description
    bannerImage
    id
    airingSchedule {
      nodes {
        airingAt
        episode
      }
    }
    recommendations {
      nodes {
        media {
          title {
            english
          }
        }
        mediaRecommendation {
          title {
            english
          }
        }
      }
    }
  }
}
'''

# Define our query variables and values that will be used in the query request
myAnilistID = 176496    # ID for "Solo Leveling S2"
variables = {
    'mediaId': myAnilistID
}

url = 'https://graphql.anilist.co'

# Make the HTTP API request
response = requests.post(url, json={'query': query, 'variables': variables}).json()
# print(response)

# data for anime general
anilist_ID = response['data']['Media']['id']
description = response['data']['Media']['description']
episodes = response['data']['Media']['episodes']
premiere = response['data']['Media']['season'] + " " + str(response['data']['Media']['seasonYear'])
title_eng = response['data']['Media']['title']['english']
title_native = response['data']['Media']['title']['native']

# data for anime files
box_image = response['data']['Media']['coverImage']['extraLarge']
splash_image = response['data']['Media']['bannerImage']

# data for media content (airing times)
next_broadcast = response['data']['Media']['airingSchedule']['nodes'][-1]['airingAt']
date = ""
try:
  timestamp = next_broadcast
  date = datetime.datetime.fromtimestamp(timestamp)  # Convert the timestamp to readable format
  date = date.strftime('%Y-%m-%d %H:%M:%S UTC')
  print(date)
except:
  date = "No airing date found"