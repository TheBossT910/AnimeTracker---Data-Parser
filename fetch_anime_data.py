# Taha Rashid
# Feburary 8, 2025
# Description: Fetches the data of an anime using the AniList API

import requests
import datetime

from database import AnimeFirebaseData

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
typical_broadcast = response['data']['Media']['airingSchedule']['nodes'][0]['airingAt']
description = response['data']['Media']['description']
episodes = response['data']['Media']['episodes']
premiere = response['data']['Media']['season'] + " " + str(response['data']['Media']['seasonYear'])
title_eng = response['data']['Media']['title']['english']
title_native = response['data']['Media']['title']['native']

# next_broadcast = response['data']['Media']['airingSchedule']['nodes'][-1]['airingAt']

# data for anime files
box_image = response['data']['Media']['coverImage']['extraLarge']
splash_image = response['data']['Media']['bannerImage']

# data for media content (airing times)
# TODO: use typical_air to display the airing time of the anime as weekday-time format
typical_air = timeConverter(typical_broadcast)
# next_air = timeConverter(next_broadcast)

# saving all current anime titles in Firebase to a set
AnimeFirebaseData.getAnimeList()
# creating a new anime document using data from the AniList API
myObj = AnimeFirebaseData()

# formating data for the anime document
details = {
    "db_version": 1,
    "title": title_eng,
    "anilist_id": anilist_ID,
    "doc_id": "",
}

general = {
    "broadcast": "",
    "category_status": "",
    "description": description,
    "episodes": episodes,
    "isFavorite": False,
    "isRecommended": False,
    "premiere": premiere,
    "rating": "",
    "title_eng": title_eng,
    "title_native": title_native,
}

files = {
    "box_image": box_image,
    "icon_image": "",
    "splash_image": splash_image,
}

# TODO: add content for all episodes
media = {
    "episodes": {},
}

animeName = str(title_eng)

# creating the anime document
isSuccess = myObj.createAnime(details, general, files, media)
print(isSuccess)