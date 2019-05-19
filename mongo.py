from pymongo import MongoClient
import pprint
from bson.json_util import dumps

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
    print('course added : 1 Id is ' + str(rec_id1.inserted_id))

if rec_id2.acknowledged:
    print('course added : 2 Id is ' + str(rec_id2.inserted_id))

# multiple insert

ary = [
        {
            "name": "Mr.Pavan",
            "eid": 24,
            "location": "Bandar"
        },
        {
            "name": "Mrs.Bindu",
            "eid": 14,
            "location": "Pilli"
        },
]

result = collection.insert_many(ary)
for obj_id in result.inserted_ids:
    print('course added : Id is ' + str(obj_id))

# find documents
find = collection.find()
for res in find:
    pprint.pprint(res)

# find documents
find = collection.find({'name':'Mr.Pavan'})
for res1 in find:
    pprint.pprint(res1)

# find documents
find = collection.find().sort('location', 1)
for res in find:
    #res.encode('ascii')
    res1 = dumps(res)
    pprint.pprint(res1)

# find documents
find = collection.find().limit(1)
for res in find:
    pprint.pprint(res)

# find documents
find = collection.find().limit(1).skip(1)
for res in find:
    res1 = dumps(res)
    pprint.pprint(res1)


# update
find1 = collection.find()
collection.update(
    {'location':'Pilli'},
    {
        '$set':{'location':'Challapalli'}
    }, multi=False
)

find = collection.find()
for res in find:
    res1 = dumps(res)
    pprint.pprint(res1)

print(collection.find({'name':'Mrs.Bindu'}).count())

collection.delete_one({'name':'Mrs.Bindu'})

print(collection.find({'name':'Mrs.Bindu'}).count())

collection.delete_many({'name':'Mrs.Bindu'})

print(collection.find({'name':'Mrs.Bindu'}).count())

print(list(collection.aggregate([{
    '$group': {
        '_id': '$name'
    }
}])))