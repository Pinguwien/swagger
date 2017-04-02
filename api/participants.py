import tinydb
from connexion import NoContent

counter = 3
prefix = "EFA-0815"

db = tinydb.TinyDB('db.json')
db.purge()
db.insert_multiple([{
    'personalid': 'EFA-0815-000001',
    'firstname': 'Irina',
    'lastname': 'Sarzew',
    'participations': [
        {
            'start_date': '2017-04-01',
            'end_date': '2018-03-31',
            'type': 'CaseManagement'
        }
    ],
    'outputindicators': {
        'CO01': True,
        'CO02': False
    }
},
    {
    'personalid': 'EFA-0815-000002',
    'firstname': 'Max',
    'lastname': 'Mustermann',
    'participations': [
        {
            'start_date': '2017-01-01',
            'end_date': '2017-03-31',
            'type': 'Microproject'
        }
    ],
    'outputindicators': {
        'CO01': True,
        'CO02': False
    }
}])


def search():
    return db.all()


def get(id):
    Participants = tinydb.Query()
    result = db.search(Participants.personalid == id)
    if not result:
        return NoContent, 404
    return result


def post(participant):
    global counter
    personalid = "{}".format(counter).zfill(6)
    p = {
        'firstname': participant.get("firstname"),
        'lastname': participant.get("lastname"),
        'personalid': "{}{}".format(prefix, personalid),
        'participations': [],
        'outputindicators': {}
    }
    db.insert(p)
    counter = counter+1
    return p, 201


def delete(id):
    Participants = tinydb.Query()
    db.remove(Participants.personalid == id)
    return NoContent, 404
