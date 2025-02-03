# Taha Rashid
# Jan 29 2025
# Description: This program is a test program to test accessing and writing to Firebase.

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
        docs = self.db.collection("animes").stream()
        
        # prints the id and the title of each document
        # for doc in docs:
        #     print(f"{doc.id} => {doc.to_dict()}")

    def getAnime(self, animeID):
        # gets a specific anime from the collection "animes"
        specificAnime = self.db.collection(f"animes/{animeID}/s1")
        animeGeneral = specificAnime.document("general").get().to_dict()

        # print(f"general => {animeGeneral}")
        # print(animeGeneral["description"])  # prints the description of the anime
        
        # fetch and return the japanaese title of the anime
        anilistID = animeGeneral["anilist_id"]
        return anilistID
    
    def updateDescription(self, animeID, newDescription = ""):
        # updates the description of the anime
        specificAnime = self.db.collection(f"animes/{animeID}/s1")
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
            "movies": {"1": mediaContent},
        }
        
        try:
            # creating the anime document
            self.db.collection("animes").document(animeName).set( {"title": animeName} )
            
            # creating the anime's subcollections for season 1
            self.db.collection(f"animes/{animeName}/s1").document("general").set(general)
            self.db.collection(f"animes/{animeName}/s1").document("files").set(files)
            self.db.collection(f"animes/{animeName}/s1").document("media").set(media)
        except:
            return False
        
        return True

# testing class
# myObj = AnimeFirebaseData()
# # get Oshi no Ko data
# myTitle = myObj.getAnime("6KaHVRxICvkkrRYsDiMY")
# print(myTitle)  # prints the title of the anime

# updated = myObj.updateDescription("6KaHVRxICvkkrRYsDiMY", "This is a new description")
# print(updated)  # prints True if the description was updated, False otherwise

# creating a new anime document
# wasCreated = myObj.createAnime("SAKAMOTO DAYS", 177709)
# print(wasCreated)