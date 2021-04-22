import requests
from posting import Posting

def get_normalized_postings():
  r = requests.get("https://data.cityofnewyork.us/resource/kpav-sd4t.json")
  jsonArray = r.json()

  #Turn the JSON into an array of Postings objects
  listings = []
  for i in range(len(jsonArray)):
    listings.append(Posting(jsonArray[i]))

  return listings