from index_files import extract, reindex

new_analyzer = {
    "analyzer": {
        "default": {
            "type": "english"
        },
        "english_bigrams": {
            "type": "custom",
            "tokenizer": "standard",
            "filter": [
                "standard",
                "lowercase",
                "porter_stem",
                "bigram_filter"
            ]
        }
    },
    "filter": {
        "bigram_filter": {
            "type": "shingle",
            "max_shingle_size": 2,
            "min_shingle_size": 2,
            "output_unigrams": False
        }
    }
}

new_mapping = {
    "properties": {
        "cast": {
            "properties": {
                "name": {
                    "type": "string",
                    "analyzer": "english",
                    "fields": {
                        "bigrammed": {
                            "type": "string",
                            "analyzer": "english_bigrams"
                        }
                    }
                }
            }
        },
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

reindex(movie_dict=extract(), mapping_settings=new_mapping, analysis_settings=new_analyzer)