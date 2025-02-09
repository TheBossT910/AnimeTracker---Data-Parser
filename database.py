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
    titles = set()
    
    def __init__(self):
        pass
        
    @classmethod
    def getAnimeList(cls):
        # gets all the documents in the collection "animes"
        docs = cls.db.collection("anime_data").stream()
        cls.titles = {doc.to_dict()['title'] for doc in docs}

    def getAnime(self, animeID):
        # gets a specific anime from the collection "animes"
        specificAnime = self.db.collection(f"anime_data/{animeID}/data")
        animeFiles = specificAnime.document("files").get().to_dict()
        
        # fetch and return the anilist ID
        anilistID = animeFiles["anilist_id"]
        return anilistID
    
    # def updateDescription(self, animeID, newDescription = ""):
    #     # updates the description of the anime
    #     specificAnime = self.db.collection(f"anime_data/{animeID}/data")
    #     animeGeneral = specificAnime.document("general").get().to_dict()
        
    #     # don't update if the new description is the same as the old one or if it's empty
    #     if (newDescription == animeGeneral["description"] or newDescription == ""):
    #         return False
        
    #     # update the description
    #     specificAnime.document("general").update({"description": newDescription})
    #     return True
    
    # method to update the number of episodes and add information for the new episode
    def updateEpisodes(self, animeID, newEpisode = -1, content = {}):
        specificAnime = self.db.collection(f"anime_data/{animeID}/data")
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
            
    def createAnime(
        self, 
        animeName,
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
            "anilist_id": "",
            "doc_id_anime": "",
            "box_image": "",
            "icon": "",
            "splash_image": "",
        },
        media = {
            'episodes': {},
        }
     ):
        
        # check if the anime already exists
        if animeName in self.titles:
            return False
            
        try:            
            # creating the anime document with a random ID
            documentID = str(uuid.uuid4()) + "PYTHON-TEST"
            self.db.collection("anime_data").document(documentID).set( {"title": animeName, "db_version": 1} )
            
            # adding anime doc id to the files subcollection
            files["doc_id_anime"] = documentID
            
            # creating the anime's data subcollections 
            self.db.collection(f"anime_data/{documentID}/data").document("general").set(general)
            self.db.collection(f"anime_data/{documentID}/data").document("files").set(files)
            self.db.collection(f"anime_data/{documentID}/data").document("media").set(media)
        except:
            return False
        
        return True

# testing class
myObj = AnimeFirebaseData()
AnimeFirebaseData.getAnimeList()

# creating a new anime document
wasCreated = myObj.createAnime("Oshi no Ko")
print(wasCreated)

# mediaContent = {
#     "air_day": "",
#     "air_time": "",
#     "description": "",
#     "name_eng": "",
#     "name_native": "",
#     "recap": "",
#     }

# myVal = myObj.updateEpisodes("b274de57-2bcc-41f0-9744-f03804704a1cPYTHON-TEST", 2, mediaContent)
# print(myVal)