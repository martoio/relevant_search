from index_files import extract, reindex

new_mapping = {
    "properties": {
        "title": {
            "type": "text",
            "analyzer": "english"
        },
        "overview": {
            "type": "text",
            "analyzer": "english"
        }
    }
}

reindex(movie_dict=extract(), mapping_settings=new_mapping)