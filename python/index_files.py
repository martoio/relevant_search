import json
import requests
import os

ELASTICSEARCH = 'http://localhost:9200'
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

def extract():
    tmdb_file = open(os.path.join(__location__, 'tmdb.json'))
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

    bulkMovies = ""

    for id, movie in movie_dict.iteritems():
        add = {
            "index": {
                "_index": "tmdb",
                "_type": "_doc",
                "_id": movie['id']
            }
        }
        bulkMovies += json.dumps(add)
        bulkMovies += "\n"
        bulkMovies += json.dumps(movie)
        bulkMovies += "\n"
    
    resp = requests.post("{TMDB_INDEX}/_bulk".format(TMDB_INDEX=TMDB_INDEX), headers=headers, data=bulkMovies)
    if resp.status_code == 200:
        print("Files index correctly!")
    else:
        print('Error during reindexing :(')

reindex(movie_dict=extract())