from SyncDB import main as create_client
from datetime import datetime


# create a client to query from SyncDB
client = create_client()

# find from collection 'PA_TreasuryRates' with filter date >= 2020-01-01, sorting from largest date to smallest, with a limit of 300 records in total
data_list = list(client.find('PA_TreasuryRates', {'date': {'$gte': datetime(2020, 1, 1)}}, sort=[('date', -1)], limit=300))
