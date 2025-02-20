# Taha Rashid
# February 20, 2025
# Fetching data from TVDB API using async functions

import asyncio
import aiohttp
import datetime
from credentials import Credentials

class TVDB_API:
    tvdb_auth_token = Credentials.tvdb_auth_token
    @classmethod
    async def getEpisode(cls, seriesID, air_date):
        # get potential dates to check
        if (air_date == None):
            return None
        airDateCurrent = datetime.datetime.fromtimestamp(air_date).strftime('%Y-%m-%d')
        airDateDown = datetime.datetime.fromtimestamp(air_date - 86400).strftime('%Y-%m-%d')
        airDateUp = datetime.datetime.fromtimestamp(air_date + 86400).strftime('%Y-%m-%d')
       
        try:
            headers = {"Authorization": f"Bearer {cls.tvdb_auth_token}"}
            lang = "eng"
            page = 0
            
            while (True):
                # fetching information
                url = f"https://api4.thetvdb.com/v4/series/{seriesID}/episodes/default/{lang}?page={page}"
                async with aiohttp.ClientSession() as session:
                    async with session.get(url, headers=headers) as response:
                        # saving information as json
                        info = await response.json()
                        info = info["data"]
                        
                        # quit the loop if there is no data
                        if len(info["episodes"]) == 0:
                            break
                        
                        # retrieve data
                        episodeCurrent = [ep for ep in info['episodes'] if ep.get('aired') == airDateCurrent]
                        episodeDown = [ep for ep in info['episodes'] if ep.get('aired') == airDateDown]
                        episodeUp = [ep for ep in info['episodes'] if ep.get('aired') == airDateUp]
                    
                        # quit the loop if we found data
                        if (len(episodeCurrent) > 0) or (len(episodeDown) > 0) or (len(episodeUp) > 0):
                            break
                        
                        # search the next page
                        page = page + 1
                
            # if we cant find any episode on the given date, check the future date for an episode, then the past date, then return None if nothing found
            if episodeCurrent:
                return episodeCurrent[0]
            elif episodeUp:
                return episodeUp[0]
            elif episodeDown:
                return episodeDown[0]
            else:
                return None
        except:
            return None
    
    @classmethod
    async def getSeason(cls, seriesID, airDate):
        # grab the current season for the given episode
        currentEpisode = await cls.getEpisode(seriesID, airDate)
        season = None
        if (currentEpisode):
            season = currentEpisode["seasonNumber"]
        
        episodes = []
        headers = {"Authorization": f"Bearer {cls.tvdb_auth_token}"}
        lang = "eng"
        page = 0
        
        while (True and season != None):
            # fetch a page of episodes from the series
            url = f"https://api4.thetvdb.com/v4/series/{seriesID}/episodes/default/{lang}?page={page}"
            async with aiohttp.ClientSession() as session:
                async with session.get(url, headers=headers) as response:
                    # saving information as json
                    info = await response.json()
                    info = info["data"]
                    
                    # exit when there is no more episodes to look at
                    if len(info["episodes"]) == 0:
                        break
                    
                    # add the episode if it is a part of the current season
                    # TODO: add a check if we have the correct # of episodes, then quit
                    for episode in info["episodes"]:
                        if episode["seasonNumber"] == season:
                            episodes.append(episode)
                    
                    # search the next page
                    page = page + 1
                    
        # return a list of episodes in the current season
        return episodes

# testing
# specific episode
# episode = asyncio.run(TVDB_API.getEpisode(389597, 1740236400))
# print(episode)

# whole season
# season = asyncio.run(TVDB_API.getSeason(389597, 1740236400))
# print(season)