import pymongo
from config import url

with pymongo.MongoClient(url) as client:
    db = client.myDataBase
    collection = db.mycollection

    cursor = collection.find({'tags' : 'python'})

    for result in cursor:
        for key, value in result.items():
            print(f'{key}: {value}')

    print(result['_id'].generation_time)