
from DevDB import main as create_client
from datetime import datetime
from pymongo.errors import BulkWriteError, DuplicateKeyError

# create a client to read from and write into DevDB
client = create_client()

# find from collection 'test_collection'
data_list = list(client.find('test_collection'))
print(data_list)

# insert a document {'name': 'banana', 'count': 1} into the test_collection
result = client.insert_one('test_collection', {'name': 'banana', 'count': 1})
print('Inserted ID: ', result.inserted_id)

# delete documents with {'count': 1} from the test_collection
result = client.delete_many('test_collection', {'count': 1})
print('Deleted Count: ', result.deleted_count)

# create a new collection named new_test_collection and insert a list of documents into it
insertion_list = [{'name': 'apple', 'count': 8},
                  {'name': 'orange', 'count': 2}]
result = client.insert_many('new_test_collection', insertion_list)
print('Inserted IDs', result.inserted_ids)

# create a descending index for column 'count' in new_test_collection
client.create_index('new_test_collection', [('count', -1)])

# drop collection 'new_test_collection'
client.drop('new_test_collection')
