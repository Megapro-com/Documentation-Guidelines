from MongoDB.client import SyncDB
import pandas as pd


# create a client to query from SyncDB
client = SyncDB

# find from collection 'LONG_BTOStock' with filter date >= 2021-10-15, sorting from largest date to smallest, with a limit of 300 records in total
data_list = list(client.find('LONG_BTOStock', {'date': {'$gte': '2021-10-15'}}, sort=[('date', -1)], limit=300))

# create a dataframe with the data list, remove _id and UpdateTime
df = pd.DataFrame(data_list).drop(['_id', 'UpdateTime'], axis=1)
print(df)
