import requests
from posting import Posting
from normalization import get_normalized_postings

class Model:
  def __init__(self):
    self.listings = get_normalized_postings()

  def get_matching_postings(self, queryString="", splitter=", "):
    pass

class Boolean_Model(Model):
  def __init__(self):
    super(Boolean_Model, self).__init__()

  def get_matching_postings(self, queryString="", splitter=", "):
    queryList = queryString.lower().split(splitter)

    matchingListings = []
    #For each listing
    for i in range(len(self.listings)):
      hasAll = True
      #Make sure all words appear
      for queryWord in queryList:
        if self.listings[i].title_NLTK.count(queryWord) == 0:
          hasAll = False
          break
      #Add to list if all appear
      if hasAll:
        matchingListings.append(self.listings[i])
    
    return matchingListings

class Vector_Model(Model):
  def __init__(self):
    super(Vector_Model, self).__init__()

  def get_matching_postings(self, queryString="", splitter=", "):
    pass