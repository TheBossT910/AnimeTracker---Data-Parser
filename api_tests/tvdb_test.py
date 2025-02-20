import aiohttp
import asyncio
from credentials import Credentials

# This is a ChatGPT example

API_KEY = Credentials.tvdb_api_key
TOKEN = Credentials.tvdb_auth_token  # Get this from /login first

async def fetch_series_id(series_name):
    url = f"https://api4.thetvdb.com/v4/search?query={series_name}"
    headers = {"Authorization": f"Bearer {TOKEN}"}

    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as response:
            data = await response.json()
            if "data" in data and data["data"]:
                return data["data"][0]["id"]  # Return the TVDB ID
            return None

async def main():
    series_list = ["Attack on Titan", "Death Note", "Jujutsu Kaisen"]
    tasks = [fetch_series_id(series) for series in series_list]
    results = await asyncio.gather(*tasks)
    
    for name, tvdb_id in zip(series_list, results):
        print(f"TVDB ID for {name}: {tvdb_id}")

asyncio.run(main())


# get TVDB auth token
# import requests

# API_KEY = ""

# def get_auth_token():
#     url = "https://api4.thetvdb.com/v4/login"
#     payload = {"apikey": API_KEY}
    
#     response = requests.post(url, json=payload)
#     data = response.json()
    
#     if "data" in data and "token" in data["data"]:
#         return data["data"]["token"]
#     return None

# # Get token
# token = get_auth_token()
# print("Auth Token:", token)