Let's start up our Elasticsearch node on Docker.
`docker run --name searchy -d -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" martoio/elasticsearch-with-phonetic:0.1.0`{{execute}}

You should be able to verify that the image runs correctly by running:
`curl localhost:9200`{{execute}}
And seeing the familiar `You know, for Search!` tagline.
