# Back to debugging!

So all that theory aside, what can we _actually_ do to change scores? We saw that the most relevant results are things that match `aliens`, `basketball`, and the word `with`. We can immediately improve results by getting rid of things like `stop words`. These words contribute to the calculation of `TF`x`IDF`, and can scew results the wrong way. We can use the default English analyzer to improve our results:
```json
"mappings": {
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
```
or run `python /root/tools/python/step7.py`{{execute}}

Going back to the Kibana dashboard, we can see the difference this made.