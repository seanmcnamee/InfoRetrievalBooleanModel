from models import Boolean_Model

model = Boolean_Model()
queries = ["Computer, .NET", "Science", "Police"]

for query in queries:
    print("Query: ", query)
    for listing in model.get_matching_postings(query):
        print("\t", listing.business_title)