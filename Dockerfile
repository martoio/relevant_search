FROM docker.elastic.co/elasticsearch/elasticsearch:7.6.1

RUN elasticsearch-plugin install analysis-phonetic

COPY ./tmdb.json ./tmdb.json