import pymongo
from config import url
import openfile

with pymongo.MongoClient(url) as client:
    db = client.Device_Configuration
    collection = db.Interfaces

    data = openfile.getInterfaces()
    #print("my data", data)

    for elem in data:
        print("-> Elem in data", elem)
        #assign elements from gathered data as document
        document = elem
        #create id
        document_id = collection.insert_one(document).inserted_id
        print(f'Created a document with id: {document_id}')

    #document_id = collection.insert_one(document).inserted_id
    #print(f'Created a document with id: {document_id}')