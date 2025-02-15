# Taha Rashid
# Jan 29 2025
# Description: Access and write to Firebase

import uuid
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

 # initialize Firebase
cred = credentials.Certificate('animetracker-201c9-firebase-adminsdk-z85u9-9cf57505ac.json')
app = firebase_admin.initialize_app(cred)
db = firestore.client()

class AnimeFirebaseData:
    # save the list of animes as anilist_ids
    titles = set()
    
    # gets all the anilist_ids and saves them to a set
    @classmethod
    def getAnimeList(cls):
        docs = db.collection("anime_data").stream()
        cls.titles = {doc.to_dict()['anilist_id'] for doc in docs}
    
    # update the number of episodes and add information for the new episode
    @classmethod
    def updateEpisodes(cls, animeID, newEpisode = -1, content = {}):
        specificAnime = db.collection(f"anime_data/{animeID}/data")
        animeMedia = specificAnime.document("media").get().to_dict()
        
        # don't update if the new episodes is the same as an old one or if it's empty or if the content is invalid
        if (newEpisode == -1): 
            # print("no new episode") 
            return False
        if (str(newEpisode) in animeMedia["episodes"]):
            # print("newEpisode already exists")
            return False
        if (len(content) != 6):
            # print("invalid content")
            return False
        
        # add the new episode
        specificAnime.document("media").set({"episodes": {f"{newEpisode}": content}}, merge=True)
        # confirms a new episode was added
        return True
    
    # creates a new anime document
    @classmethod
    def createAnime(
        cls, 
        details = {
        "db_version": 1,
        "title": "",
        "anilist_id": "",
        "doc_id": "",
        },
        general = {
            "broadcast": "",
            "category_status": "",
            "description": "",
            "episodes": 0,
            "isFavorite": False,
            "isRecommended": False,
            "premiere": "",
            "rating": "",
            "title_eng": "",
            "title_native": "",
            },
        files = {
            "box_image": "",
            "icon_image": "",
            "splash_image": "",
        },
        media = {
            'episodes': {},
        }
     ):
        
        # check if the anime already exists
        if details["anilist_id"] in cls.titles:
            return False
            
        try:            
            # creating the anime document with a random ID
            documentID = str(uuid.uuid4())
            # adding anime doc id to the files subcollection
            details["doc_id"] = documentID
            # creating the main anime document
            db.collection("anime_data").document(documentID).set(details)
            
            # creating the anime's data subcollections 
            db.collection(f"anime_data/{documentID}/data").document("general").set(general)
            db.collection(f"anime_data/{documentID}/data").document("files").set(files)
            db.collection(f"anime_data/{documentID}/data").document("media").set(media)
        except:
            return False
        
        return True

# testing class
# AnimeFirebaseData.getAnimeList()
# AnimeFirebaseData.createAnime()
# AnimeFirebaseData.getAnimeList()