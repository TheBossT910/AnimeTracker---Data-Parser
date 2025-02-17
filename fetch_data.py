# Taha Rashid
# February 15, 2025
# Description: Fetchs new/updated anime data via AniList API using GraphQL

import requests
import datetime
from anime_id import load_json_as_dict, find_id
from database import AnimeFirebaseData
from tvdb import TVDB_API

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
    
    # private method
    @classmethod
    def getShow(cls, animeData, lookup_dict):
        main = {
          "anilist_id": "",
          "tvdb_id": "",
          "relation_id": "",
          "doc_id": "",
          "db_version": "1",
          "title": "",
          }
          
        general = {
          "description": "",
          "episodes": 0,
          "premiere": "",
          "rating": "",
          "title_english": "",
          "title_native": "",
          }
          
        files = {
          "box_image": "",
          "icon_image": "",
          "splash_image": "",
          }
          
          # putting data into general
        general["description"] = animeData["description"] #if not "null" else "N/A"
        general["episodes"] = animeData["episodes"] #if not "null" else 0
        
          
        premiere = "N/A"
        if (animeData["season"] and animeData["seasonYear"]):
          premiere = animeData["season"].capitalize() + " " + str(animeData["seasonYear"])
        general["premiere"] = premiere
          
        title_english = "N/A"
        if (animeData["title"]["english"]):
          title_english = animeData["title"]["english"]
        elif (animeData["title"]["romaji"]):
          title_english = animeData["title"]["romaji"]
        general["title_english"] = title_english
          
        general["title_native"] = animeData["title"]["native"] #if not "null" else "N/A"
        # print(general)
        
         # putting data into files
        files["box_image"] = animeData["coverImage"]["extraLarge"] #if not "null" else "N/A"
        files["splash_image"] = animeData["bannerImage"] #if not "null" else "N/A"
        # print(files)
          
         # adding main document details
        main["anilist_id"] = animeData["id"]
        main["tvdb_id"] = find_id(main["anilist_id"], lookup_dict)  
        main["relation_id"] = ""
        main["doc_id"] = ""
        main["title"] = general["title_english"]
        # print(main)
          
        response = {
          "main": main,
          "general": general,
          "files": files,
          }
        
        return response
      
    # private method, __
    @classmethod
    def getAiringSchedule(cls, page, airingAtGreater, airingAtLesser):
        # we want to get the Unix air date, and the anilist ID of the anime that is airing
        # the way our UI will work is that it will display the recap of the show, and then when you click it in the schedule it takes you to the show and automatically loads the latest episode
        # we pass in a parameter somehwere that just says load latest episode. This makes it so that we DON'T need to know the episode id, we just always load the latest episode!
        # whenever we parse this, we also want to create the related episode field (with all of its related information) in Firebase 
        # TODO: get the show's season (for when we want to grab data via TVDB)
        
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
        id
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
        parsedData = []
        response = requests.post(cls.url_anilist, json={'query': query, 'variables': variables}).json()
        rawData = response["data"]["Page"]["airingSchedules"]
        hasNextPage = True
        
        while (hasNextPage):
          for anime in rawData:
            episode = {
              "title_show": "", # this is the show's title
              "title_episode": "",
              "anilist_id": 0,  # this also refers to the doc id
              "tvdb_id": 0,     # this also refers to the episode id
              "broadcast": 0,    # Unix broadcast time
              "box_image": "",
              "runtime": 0,
              "description": "",
              "recap": ""             
            }
            
            titleShow = "N/A"
            if (anime["media"]["title"]["english"]):
              titleShow = anime["media"]["title"]["english"]
            elif (anime["media"]["title"]["romaji"]):
              titleShow = anime["media"]["title"]["romaji"]
            elif (anime["media"]["title"]["native"]):
              titleShow = anime["media"]["title"]["english"]
            episode["title_show"] = titleShow
            
            episode["anilist_id"] = anime["media"]["id"]
            episode["broadcast"] = anime["airingAt"]
            
            # print(episode)
            
            # TODO: Also scrape each episode's info on TVDB. If a show does not exist, we want to run a function to specifically create that show. 
            # We will look up the show in Firebase using the AniList ID, and get the the TVDB id, then scrape the selected episode using that!
            # We can select the correct season (and specifically the correct episode) by searching through all episodes for the matching air date of the episode.
            # method to grab info from FB. if "false", then we create a new episode
            fetchedAnime = AnimeFirebaseData.fd_getAnime(str(episode["anilist_id"]))
            if (fetchedAnime == None):
              newAnimeQuery = '''
query Media($mediaId: Int) {
  Media(id: $mediaId) {
      title {
        english
        native
        romaji
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
  }
}
              '''
              newAnimeVariables = {
                "mediaId": episode["anilist_id"]
              }
              newAnimeResponse = requests.post(cls.url_anilist, json={'query': newAnimeQuery, 'variables': newAnimeVariables}).json()
              # print(newAnimeResponse)
              animeData = newAnimeResponse["data"]["Media"]
              
              file_path = "anime-list-full.json"
              lookup_dict = load_json_as_dict(file_path)
              newAnimeParsedData = cls.getShow(animeData, lookup_dict)
              # print(newAnimeParsedData)
              AnimeFirebaseData.fd_addAnime(newAnimeParsedData["main"], newAnimeParsedData["general"], newAnimeParsedData["files"])
            
            # look up the anime
            tvdbID = AnimeFirebaseData.fd_getAnime(episode["anilist_id"])["tvdb_id"]
            episode["tvdb_id"] = tvdbID
            formattedDate = datetime.datetime.fromtimestamp(int(episode["broadcast"])).strftime('%Y-%m-%d')
            # TODO: run function to scrape from tvdb
            episodeInfo = TVDB_API.getEpisode(tvdbID, formattedDate)
            if (episodeInfo):
              # print(episodeInfo)
              episode["title_episode"] = episodeInfo["name"]
              episode["box_image"] = "https://artworks.thetvdb.com" + episodeInfo["image"]
              episode["description"] = episodeInfo["overview"]
              episode["runtime"] = episodeInfo["runtime"]
              # print(episode)
              AnimeFirebaseData.fd_addEpisode(episode["anilist_id"], episode["tvdb_id"], episode)
              
            parsedData.append(episode)
            
              
            
          # getting the next page
          variables["page"] = variables["page"] + 1
          response = requests.post(cls.url_anilist, json={'query': query, 'variables': variables}).json()
          rawData = response["data"]["Page"]["airingSchedules"]
          hasNextPage = response["data"]["Page"]["pageInfo"]["hasNextPage"]
        
        return parsedData

    @classmethod
    def getNewlyAdded(cls, page, startDateGreater):
      # returns a list of main, general, and files objects with parsed data for all newly added animes
      
      # AniList API
      # TODO: keep looping and parsing data until hasNextPage = false
      query = ''' 
query Page($page: Int, $perPage: Int, $startDateGreater: FuzzyDateInt, $format: MediaFormat) {
  Page(page: $page, perPage: $perPage) {
    media(startDate_greater: $startDateGreater, format: $format) {
      title {
        english
        native
        romaji
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
      
      # get response from AniList
      response = requests.post(cls.url_anilist, json={'query': query, 'variables': variables}).json()
      # print(response)
      
      # saving all of our parsed data in an array
      parsedData = []
      file_path = "anime-list-full.json"
      lookup_dict = load_json_as_dict(file_path)  
      
      rawData = response["data"]["Page"]["media"]
      hasNextPage = True
      while (hasNextPage):
        # print(hasNextPage)
        # print(rawData)
        
        for anime in rawData:
          response = cls.getShow(anime, lookup_dict)
          parsedData.append(response)
          
        # getting the next page of data
        variables["page"] = variables["page"] + 1
        # print(variables["page"])
        response = requests.post(cls.url_anilist, json={'query': query, 'variables': variables}).json()
        rawData = response["data"]["Page"]["media"]
        hasNextPage = response["data"]["Page"]["pageInfo"]["hasNextPage"]
        
      return parsedData
    
    @classmethod
    def getAiringWeek(cls, page, weekStart):
        # uses getAiringSchedule, 1 week interval
        # weekStart is a Unix timestamp, 
        # 604,800 sec/week
        weekEnd = weekStart + 604800
        response = cls.__getAiringSchedule(page, weekStart, weekEnd)
        return response
    
    @classmethod
    def getAiringDay(cls, page, dayStart):
        # uses getAiringSchedule, 1 day interval (00:00 -> 24:00)
        # 86,400 sec/day
        dayEnd = dayStart + 86400
        response = cls.__getAiringSchedule(page, dayStart, dayEnd)
        return response
    
    # TODO: implement
    @classmethod
    def updateNextAir(cls, oldDayAir):
        # Need to know the structure of oldDayAir to do anything here...  
        pass
    
    # TODO: implement
    @classmethod
    def cleanOldData(cls, oldWeekAir):
        # Need to know the structure of oldWeekAir to do anything here... Should I make it the same structure as oldDayAir??
        pass
    





import timeit
start = timeit.timeit()

temp = FetchData.getAiringSchedule(1, 1739595600, 1739682000)

end = timeit.timeit()
print(end - start)

print(len(temp))

# print(myData)
# Unix timestamps

# temp = FetchData.getAiringWeek(1, 1738990800)
# temp = FetchData.getAiringDay(1, 1739682000)
# print(temp)
# FetchData.getAiringDay(1, 1738990800)
# FetchData.getAiringWeek(1, 1738990800)