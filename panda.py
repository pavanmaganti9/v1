import pandas as pd
import numpy as np
from pymongo import MongoClient

xl = pd.read_excel('store.xls',index=False)

oid = pd.Series(xl['Order ID'])
name = pd.Series(xl['Customer Name'])

oid = list(oid.head(10))
name1 = list(name.head(10))

s = pd.Series(oid, index=name1)

print s

print name1
#print oid.describe()
d = s.to_dict()
print d

# simple array
data = ['Pavan','Bindu']

ser = pd.Series(data)
print(ser)

#reading from sheets

sheet = pd.read_excel(open('store.xls','rb'),sheet_name='People')

sheet_data = pd.Series(sheet['Person'])

print sheet_data

client = MongoClient('mongodb://localhost', 27017)
db = client.version1
collection = db.sample1
