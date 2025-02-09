# Taha Rashid
# Jan 29 2025
# Description: This program is a test program to test accessing and writing to Firebase.

import uuid
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

class AnimeFirebaseData:
    # Use a service account.
    cred = credentials.Certificate('animetracker-201c9-firebase-adminsdk-z85u9-9cf57505ac.json')
    app = firebase_admin.initialize_app(cred)
    db = firestore.client()
    
    def __init__(self):
        # gets all the documents in the collection "animes"
        docs = self.db.collection("anime_data").stream()

    def getAnime(self, animeID):
        # gets a specific anime from the collection "animes"
        specificAnime = self.db.collection(f"anime_data/{animeID}/data")
        animeFiles = specificAnime.document("files").get().to_dict()
        
        # fetch and return the anilist ID
        anilistID = animeFiles["anilist_id"]
        return anilistID
    
    def updateDescription(self, animeID, newDescription = ""):
        # updates the description of the anime
        specificAnime = self.db.collection(f"anime_data/{animeID}/data")
        animeGeneral = specificAnime.document("general").get().to_dict()
        
        # don't update if the new description is the same as the old one or if it's empty
        if (newDescription == animeGeneral["description"] or newDescription == ""):
            return False
        
        # update the description
        specificAnime.document("general").update({"description": newDescription})
        return True
    
    def createAnime(self, animeName, anilistID):
        general = {
            "anilist_id": anilistID,
            "broadcast": "",
            "category_status": "",
            "description": "",
            "episodes": 0,
            "isFavorite": False,
            "isRecommended": False,
            "premiere": "",
            "rating": "",
            "title_eng": "",
            "title_jp": "",
        }
        
        files = {
            "box_image": "",
            "doc_id_anime": "",
            "icon": "",
            "splash_image": "",
        }
        
        mediaContent = {
            "air_day": "",
            "air_time": "",
            "description": "",
            "name_eng": "",
            "name_jp": "",
            "recap": "",
        }
        
        media = {
            "episodes": {"1": mediaContent},
            # "movies": {"1": mediaContent},
        }
        
        try:
            # creating the anime document
            documentID = str(uuid.uuid4()) + "PYTHON-TEST"
            self.db.collection("anime_data").document(documentID).set( {"title": animeName, "db_version": 1} )
            
            # creating the anime's subcollections for season 1
            self.db.collection(f"anime_data/{documentID}/data").document("general").set(general)
            self.db.collection(f"anime_data/{documentID}/data").document("files").set(files)
            self.db.collection(f"anime_data/{documentID}/data").document("media").set(media)
        except:
            return False
        
        return True

# testing class
myObj = AnimeFirebaseData()

# creating a new anime document
# wasCreated = myObj.createAnime("SAKAMOTO DAYS", 177709)
# print(wasCreated)

myVal = myObj.updateEpisodes("b274de57-2bcc-41f0-9744-f03804704a1cPYTHON-TEST", 0)
print(myVal)