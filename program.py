from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017") 
print(client)

# alldatabases = client.list_database_names()
# print(alldatabases)

#insertOne & insertmany
#insertone = insertonedocument(single doc)
#insertone = insertmultidocument(multi doc)

database = client["Demo1"] #creating new database as demo1
collection1 = database["myCollection"] #creating new collection in demo1


# #insertone 
dictionary = {"name": "Anjum","age": 24, "location": "Kolhapur"}
collection1.insert_one(dictionary)

#now insertmanyfunction
# To insertmanyfunction we need to create a list first.abs
# after creating list give dictionary inside that list
insertList = [
    {"name": "Anjum", "age": 22, "location": "kop"},
    {"name": "Anjum", "age": 21, "location": "goa"},
    {"name": "vijay", "age": 20, "location": "delhi"},
    {"name": "pakkya", "age": 23, "location": "mumbai"},
    {"name": "shambhu", "age": 24, "location": "pune"}
]

collection1.insert_many(insertList)
# if we dont give id to our list then by deafult mongoDB will give
#we can also give id to this by adding id in dict as "_id": 1 so on

"""
Now to read data

"""

read = collection1.find_one({"name": "pakkya"}) #find_one = find single doc
print(read)

# to get all the doc at same time
allDocs = collection1.find({"name": "Anjum"}) #find = find all doc
for item in allDocs:
    print(item)


#For Updating The Data
"""
in update data there are 2 funtion : update_one & update_many
    
"""
#update One
# we need to give or we need to give id from where we wanted to update the data

prev = {"name": "Anjum"}
next = {"$set": {"location": "Hyd"}}

modified = collection1.update_one(prev,next)

#update many or update all doc

prev = {"name": "Anjum"}
next = {"$set": {"location": "Hyd"}}

modified = collection1.update_many(prev,next)


#Delete data
# delete one
# delete many

# #delete one
doc = {"name": "Anjum"}
collection1.delete_one(doc)

#delete many

doc = {"name": "Anjum"}
collection1.delete_many(doc)





