# Taha Rashid
# February 15, 2025
# Description: Fetchs new/updated anime data via AniList API using GraphQL

import requests

class FetchData:
    # TODO:
    # All of these functions will be class methods, meaning that we don't need to create objects
    # getNewlyAdded (bi-weekly basis, gets newly added shows)
    
    # getCurrentlyAiring (weekly basis, grabs the currently airing shows and their next air time, and the predicted air time after that (we grab 2 air times?))
    # checkAiringToday (daily basis, checks if the info for shows airing today has changed)
        # These fns can use the same base code, just change the "times" we want to look between
        
    # updateNextAir (daily basis, updates the next air date for shows that aired the previous day. Runs before checkAiringToday)
        # this looks through the old "airing today" data, and runs their ids to get the next airing day. Very simple
    # cleanOldData (weekly basis, deletes show air data that is >2 weeks old)
    
    url_anilist = 'https://graphql.anilist.co'
    
    @classmethod
    def getNewlyAdded(cls, page, startDateGreater):
        query = '''
query Page($page: Int, $perPage: Int, $startDateGreater: FuzzyDateInt, $format: MediaFormat) {
  Page(page: $page, perPage: $perPage) {
    media(startDate_greater: $startDateGreater, format: $format) {
      title {
        english
        native
        romaji
      }
    }
    pageInfo {
      hasNextPage
    } 
  }
}
        '''
        variables = {
        "page": page,
        "perPage": 50,
        "startDateGreater": startDateGreater,
        # TODO: Select between different formats
        "format": "TV",
        }
        response = requests.post(cls.url_anilist, json={'query': query, 'variables': variables}).json()
        print(response)
        rawData = response.data.Page.media
        hasNextPage = response.data.Page.pageInfo.hasNextPage
        # TODO: keep looping and parsing data until hasNextPage = false
        
        # TODO: return filtered data? Call fn!
        pass
    
    # private method, __
    @classmethod
    def __getAiringSchedule(cls, page, airingAtGreater, airingAtLesser):
        query = '''
query AiringSchedules($page: Int, $perPage: Int, $notYetAired: Boolean, $airingAtGreater: Int, $airingAtLesser: Int) {
  Page(page: $page, perPage: $perPage) {
    airingSchedules(notYetAired: $notYetAired, airingAt_greater: $airingAtGreater, airingAt_lesser: $airingAtLesser) {
      episode
      media {
        title {
          english
          native
          romaji
        }
      }
      airingAt
    }
    pageInfo {
      hasNextPage
    }
  }
}
        '''
        variables = {
        "page": page,
        "perPage": 50,
        "notYetAired": False,
        "airingAtGreater": airingAtGreater,
        "airingAtLesser": airingAtLesser,
        }
        response = requests.post(cls.url_anilist, json={'query': query, 'variables': variables}).json()
        print(response)
        # TODO: return filtered data?, call fn!
        pass
        
    
    @classmethod
    def getAiringWeek(cls, page, weekStart):
        # uses getAiringSchedule, 1 week interval
        # weekStart is a Unix timestamp, 
        # 604,800 sec/week
        weekEnd = weekStart + 604800
        response = cls.__getAiringSchedule(page, weekStart, weekEnd)
        print(response)
        # TODO: return filtered data, call fn!
        pass
    
    @classmethod
    def getAiringDay(cls, page, dayStart):
        # uses getAiringSchedule, 1 day interval (00:00 -> 24:00)
        # 86,400 sec/day
        dayEnd = dayStart + 86400
        response = cls.__getAiringSchedule(page, dayStart, dayEnd)
        print(response)
        # TODO: return filtered data, call fn!
        pass
    
    # TODO: implement
    @classmethod
    def updateNextAir(cls, oldDayAir):
        # Need to know the structure of oldDayAir to do anything here...
        for anime in oldDayAir:
            currentAnimeID = anime.animeID
            currentAiringDate = anime.airingDate
            
            
        pass
    
    # TODO: implement
    @classmethod
    def cleanOldData(cls, oldWeekAir):
        # Need to know the structure of oldWeekAir to do anything here... Should I make it the same structure as oldDayAir??
        pass
    







FetchData.getNewlyAdded(3, 20250101)
# Unix timestamps
# FetchData.getAiringSchedule(3, 1738990800, 1740286800)
# FetchData.getAiringDay(1, 1738990800)
# FetchData.getAiringWeek(1, 1738990800)


# Saving rough GraphQL queries
'''
Gets a page of the animes airing between 00:00 Feb 15 and 24:00 Feb 15 (Basically on Feb 15)
This can be used to grab animes airing daily AND animes airing a week after/before. Just need to adjust the times that we want to look between

query AiringSchedules($page: Int, $perPage: Int, $notYetAired: Boolean, $airingAtGreater: Int, $airingAtLesser: Int) {
  Page(page: $page, perPage: $perPage) {
    airingSchedules(notYetAired: $notYetAired, airingAt_greater: $airingAtGreater, airingAt_lesser: $airingAtLesser) {
      episode
      media {
        title {
          english
          native
          romaji
        }
      }
      airingAt
    }
    pageInfo {
      hasNextPage
    }
  }
}

HEADER
{
  "page": 3,
  "perPage": 50,
  "notYetAired": false,
  "airingAtGreater": 1738990800,
  "airingAtLesser": 1740286800,
}
'''

# We could get airing animes by filitering based on season (Winter 2025, etc.)
# actually, base it on "Start date greater than" and input the start date to be the last date you previously checked from
'''
Get newly added animes

query Page($page: Int, $perPage: Int, $startDateGreater: FuzzyDateInt, $format: MediaFormat, $airingAtGreater: Int) {
  Page(page: $page, perPage: $perPage) {
    media(startDate_greater: $startDateGreater, format: $format) {
      title {
        english
        native
        romaji
      }
    }
    pageInfo {
      hasNextPage
    } 
  }
}

HEADER
{
  "page": 3,
  "perPage": 50,
  "startDateGreater": 20250101,
  "format": "TV",
}
'''