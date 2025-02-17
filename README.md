# AnimeTracker - Data Parser
This code is meant to collect Anime data from different sources and import them into Firebase. 
* Currently I am only using AniList API

**PLAN**
* Get show general data
* Get show files (image URLs)
* Get air times
* Be able to create a new Firebase entry if the show does not exist yet


## Organization (my plan for this)
* ai_recap.py -> AI recap of shows
* database.py -> Firebase
* fetch_data.py -> grabs anime data
* update_data.py -> uses fetch_data and database to get the new data and push the updates to Firebase (the file that connects everything together)

## TODO
* Figure out what data we want
* Integrate anime-lists (https://github.com/Fribb/anime-lists) as a sub repo, and use it!