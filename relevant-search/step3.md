# Let's see some action!

### Clone the repo with all the tools
To begin, we're going to need a few tools. In the terminal, run `./course/init.sh`{{execute}} (Tip: click on the code block!)

### Spin up an Elasticsearch Docker container
Let's start up our Elasticsearch node on Docker.
`docker run --name searchy -d -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" martoio/elasticsearch-with-phonetic:0.1.0`{{execute}}

### Spin up Kibana
Let's also spin up a Kibana instance so we can use the tools there as well.
`docker run -d --name kibana --link searchy:elasticsearch -p 5601:5601 docker.elastic.co/kibana/kibana:7.6.1
`{{execute}}

### Verify it's all good
Running `docker ps`{{execute}} should give you the running docker containers named `searchy` and `kibana`.

You should be able to verify that the container runs correctly by running:
`curl localhost:9200`{{execute}}
And seeing the familiar `You know, for Search!` tagline.

### Spin up the dashboard
We have a frontend dashboard built to make some of the visualizations a little easier, and so that we don't have to read all of the verbose JSON output from Elasticsearch. To spin up the dashboard, just run: <br>
`cd dashboard && npm install && npm start`{{execute}}

