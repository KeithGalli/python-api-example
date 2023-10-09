import os 
from pyairtable import Api

API_TOKEN = os.environ.get('AIRTABLE_TOKEN')

BASE_ID = 'appi1uzlLKn1TEKSw'
TABLE_ID = 'tblvMMAVHo901m2Ra'

api = Api(API_TOKEN)

table = api.table(BASE_ID, TABLE_ID)

def get_all_records(count=None, sort=None):
    sort_param = []
    if sort and sort.upper()=='DESC':
        sort_param = ['-Rating']
    elif sort and sort.upper()=='ASC':
        sort_param = ['Rating']

    return table.all(max_records=count, sort=sort_param)

def get_record_id(name):
    return table.first(formula=f"Book='{name}'")['id']

def update_record(record_id, data):
    table.update(record_id, data)

    return True

def add_record(data):
    # require data contains a "Book" key and a "Rating" key (data is a dict)
    if 'Book' not in data or 'Rating' not in data:
        return False

    table.create(data)
    return True

if __name__ == '__main__':
    ## Show getting certain records
    print("Show getting certain records")
    print(table.all(formula="Rating < 5", sort=['-Rating']))

    ## Show getting a single record
    print("Show getting a single record")

    # Replace a record
    print("Replace a record")
    name = "Test Message"
    record_id = table.first(formula=f"Book='{name}'")['id']
    table.update(record_id, {"Rating": 5})

    ## Show all records
    print("All records!")
    print(table.all())