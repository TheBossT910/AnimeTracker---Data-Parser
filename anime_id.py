# Taha Rashid 
# Feburary 16, 2025
# Parse list of anime ids. Courtesy of ChatGPT

import json

def load_json_as_dict(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)  # Load everything into memory
        return {
            obj.get("anilist_id"): obj.get("thetvdb_id") 
            for obj in data 
            if obj.get("anilist_id") is not None  # Ensure we only include objects with an anilist_id
        }

def find_id(target_id, lookup_dict):
    return lookup_dict.get(target_id)  # O(1) lookup

# Load once into memory
# file_path = "anime-list-full.json"
# lookup_dict = load_json_as_dict(file_path)  

# Now lookups are instant
# import timeit
# start = timeit.timeit()
# result = find_id(176496, lookup_dict)  
# end = timeit.timeit()
# print(end - start)
# print(result) 
    
