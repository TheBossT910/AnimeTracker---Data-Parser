# Taha Rashid
# February 16, 2025
# Testing TVDB

import tvdb_v4_official
# import time
import datetime
from credentials import Credentials

tvdb = tvdb_v4_official.TVDB(Credentials.tvdb_api_key)
# See https://github.com/thetvdb/v4-api

class TVDB_API:
    @classmethod
    def getEpisode(cls, seriesID, air_date):
        airDateCurrent = datetime.datetime.fromtimestamp(air_date).strftime('%Y-%m-%d')
        airDateDown = datetime.datetime.fromtimestamp(air_date - 86400).strftime('%Y-%m-%d')
        airDateUp = datetime.datetime.fromtimestamp(air_date + 86400).strftime('%Y-%m-%d')
        try:
            page = 0
            while (True):
                # fetch a page of episodes from a series by season_type (type is "default" if unspecified)
                info = tvdb.get_series_episodes(id=seriesID, page=page, lang="eng")
                # print(info['episodes'])
                
                # quit the loop if there is no data
                if len(info['episodes']) == 0:
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
    def getSeason(cls, seriesID, air_date):
        # TODO: only return episodes that have aired (check against current date)
        # grabs the info for 1 episode
        currentEpisode = cls.getEpisode(seriesID, air_date)
        if (currentEpisode):
            season = currentEpisode["seasonNumber"]
        else:
            season = None
        
        episodes = []
        page = 0
        
        while(True and season != None):        
            # fetch a page of episodes from a series by season_type (type is "default" if unspecified)
            info = tvdb.get_series_episodes(id=seriesID, page=page, lang="eng")
            
            # exit when there is no more episodes to look at
            if len(info["episodes"]) == 0:
                break
            
            for episode in info['episodes']:
                if episode["seasonNumber"] == season:
                    # convert the broadcast date to Unix timestamp
                    # rawBroadcast = episode["aired"]
                    # broadcast = time.mktime(datetime.datetime.strptime(rawBroadcast, "%Y-%m-%d").timetuple())
                    # episode["aired"] = broadcast
                    episodes.append(episode)
            
            # search the next page
            page = page + 1
        
        return episodes
        
# 389597, 1740236400
# temp = TVDB_API.getEpisode(72454, 1739595600)
# temp = TVDB_API.getSeason(389597, 1740236400)
# print(temp)
