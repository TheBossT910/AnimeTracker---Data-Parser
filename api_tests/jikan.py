# Taha Rashid
# February 16, 2025
# Testing out the Jikan API

from jikanpy import Jikan
jikan = Jikan()

response = jikan.anime(58567)
# mushishi_with_eps = jikan.anime(457, extension='episodes')
# search_result = jikan.search('anime', 'Mushishi', page=2)
# winter_2018_anime = jikan.seasons(year=2018, season='winter')
# current_season = jikan.seasons(extension='now')

print(response)