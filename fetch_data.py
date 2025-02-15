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
    # updateNextAir (daily basis, updates the next air date for shows that aired the previous day. Runs before checkAiringToday)
    # cleanOldData (weekly basis, deletes show air data that is >2 weeks old)
    