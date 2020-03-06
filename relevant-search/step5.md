# Let's search!

## Before search, there was data
So let's index some data in our cluster. The data file we are using is a slice of the TMDB database. The JSON for this was provided by the authors of the book _Relevant Search_ on the [GitHub page for the book](https://github.com/o19s/relevant-search-book).

We have some handy python scripts in our `python` folder to help with getting the data into our ES index. First, let's run `/root/tools/python/init.sh`{{execute}}

Then let's run `source /root/tools/python/virtualenv/bin/activate`{{execute}}<br>
and  `pip install -r /root/tools/python/requirements.txt`{{execute}}

After everything is setup, we can run `python /root/tools/python/index_files.py`{{execute}}. This will delete any previous `tmdb` index and create a new one, and then upload the data from the JSON file to Elasticsearch.

## Search in Kibana
Make sure your Kibana console is available and let's try running some queries! Go to the Dev Tools and and the following:
```json
GET /tmdb/_search
{
    "query": {
        "multi_match": {
            "query": "basketball with cartoon aliens",
            "fields": ["title^10", "overview"]
        }
    },
    "_source": "title",
    "size": 100
}
```
If you haven't guessed it, we're trying to find the movie `Space Jam`

What happened? _Space Jam_ is way down in the search and a bunch of seemingly random movies outrank it. Let's debug.

## Explain
A great start in this case is seeing the Lucene query that is actually going to get run. To do that, we can execute the following:
```json
GET /tmdb/_validate/query?explain
{
    "query": {
        "multi_match": {
            "query": "basketball with cartoon aliens",
            "fields": ["title^10", "overview"]
        }
    }
}
```

The result is this:
```
((overview:basketball overview:with overview:cartoon overview:aliens) | (title:basketball title:with title:cartoon title:aliens)^10.0)
```
The first clause searches for each _term_ in the _**overview**_ field. The Second clause search for each _term_ in the _**title**_ field and the score is boosted by a factor of 10. The `|` charachter here represents `MAXOF` - essentially taking the clause that returns the higher score.

## Checking out tokens
Let's take a seemingly random search result and run it through the analyzer. What tokens are actually inside the inverted index?
```json
GET /tmdb/_analyze
{
    "analyzer": "standard",
    "text":"Fire with Fire"
}
```

We see that each of the three words ends up as a token. This means that the term `with` is present in our index. Going back to the query explanation, we can start to see a potential culprit (first clause redacted):
<pre>
((...) | (title:basketball <b>title:with</b> title:cartoon title:aliens)^10.0)
</pre>
We're looking for the term `with` in the title and multiplying the result by 10!

## Show me the math
The next step in debugging is usually figuring out why a search result got a particular score. The actual value of the score itself is less important than the math Elasticsearch used to get the number. Fortunately, this is easy to do in Elasticsearch. If you have a query, all you need to add is the `"explain": true` to the top level of the query to see the logic:
<pre>
GET /tmdb/_search
{
    <b>"explain": true</b>,
    "query": {
        "multi_match": {
            "query": "basketball with cartoon aliens",
            "fields": ["title^10", "overview"]
        }
    },
    "_source": "title",
    "size": 100
}
</pre>