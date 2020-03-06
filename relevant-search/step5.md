# Let's search!

## Before search, there was data
So let's index some data in our cluster. The data file we are using is a slice of the TMDB database. The JSON for this was provided by the authors of the book _Relevant Search_ on the [GitHub page for the book](https://github.com/o19s/relevant-search-book).

We have some handy python scripts in our `python` folder to help with getting the data into our ES index. First, let's run `/root/tools/python/init.sh`{{execute}}
This will setup a `virtualenv`, and pull down some requirements for us.

After everything is setup, we can run `python /root/tools/python/index_files.py`{{execute}}. This will delete any previous `tmdb` index and create a new one, and then upload the data from the JSON file to Elasticsearch.