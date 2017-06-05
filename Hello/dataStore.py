
from flask import current_app
from google.cloud import datastore


builtin_list = list


def init_app(app):
    pass


def get_client():
    return datastore.Client(current_app.config['PROJECT_ID'])

def update(data, id=None):
    ds = get_client()
    if id:
        key = ds.key('junk', int(id))
    else:
        key = ds.key('junk')

    entity = datastore.Entity(
        key=key,
        exclude_from_indexes=['description'])

    entity.update(data)
    ds.put(entity)



create = update

