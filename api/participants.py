import tinydb
import ujson

db = tinydb.TinyDB('db.json')
db.purge()
db.insert_multiple([{
    'personalid': 'EFA-0815-0000001',
    'firstname': 'Irina',
    'lastname': 'Sarzew',
    'participations': [
        {
            'start_date': '2017-04-01',
            'end_date': '2018-03-31',
            'type': 'CaseManagement'
        }
    ],
    'outputindicators': [
        {
            'CO01': True,
            'CO02': False
        }
    ]},
    {
    'personalid': 'EFA-0815-0000002',
    'firstname': 'Max',
    'lastname': 'Mustermann',
    'participations': [
        {
            'start_date': '2017-01-01',
            'end_date': '2017-03-31',
            'type': 'Microproject'
        }
    ],
    'outputindicators': [
        {
            'CO01': True,
            'CO02': False
        }
    ]
}])


def search():
    return db.all()


def get(id):
    Participants = tinydb.Query()
    return ujson.dumps(db.search(Participants.personalid == id))
