from pymongo import MongoClient

client = MongoClient('mongodb://localhost', 27017)

# Get the sampleDB database
db = client.version1
collection = db.sample

emp_rec1 = {
    "name": "Mr.Geek",
    "eid": 24,
    "location": "delhi"
}
emp_rec2 = {
    "name": "Mr.Shaurya",
    "eid": 14,
    "location": "delhi"
}

# Insert Data
rec_id1 = collection.insert_one(emp_rec1)
rec_id2 = collection.insert_one(emp_rec2)

if rec_id1.acknowledged:
    print('course added : 1 Id is '+ str(rec_id1.inserted_id))

if rec_id2.acknowledged:
    print('course added : 2 Id is '+ str(rec_id2.inserted_id))