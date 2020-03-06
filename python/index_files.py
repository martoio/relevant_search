import json
import requests

ELASTICSEARCH = 'http://localhost:9200'

def extract():
    tmdb_file = open('tmdb.json')
    if tmdb_file:
        return json.loads(tmdb_file.read())


def reindex(analysis_settings = {}, mapping_settings = {}, movie_dict = {}):
    TMDB_INDEX = '{elasticsearch}/tmdb'.format(elasticsearch=ELASTICSEARCH)
    headers = {
        'Content-Type': 'application/json'
    }
    settings = {
        "settings": {
            "number_of_shards": 1,
            "number_of_replicas": 0,
            "index": {
                "analysis": analysis_settings
            }
        }
    }

    if mapping_settings:
        settings['mappings'] = mapping_settings
    
    print('Deleting old TMDB index...')
    resp = requests.delete(TMDB_INDEX)
    if resp.status_code == 200:
        print("TMDB index deleted successfully")

    resp = requests.put(TMDB_INDEX, headers=headers, data=json.dumps(settings))

    if resp.status_code == 200:
        print("tmdb index created successfully")


reindex()