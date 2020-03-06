# Multifield search

Elasticsearch and Lucene have 2 flavors of multi-field search:
- <b>field-centric</b> - the search runs against each specified field in isolation. The results are then combined to produce the score;
- <b>term-centric</b> - Each field is searched on a term-by-term basis. This produces a per-term score that combines the influence from each field on the specific term;

# Term-centric:
<details>
    <summary>Illustration</summary>
    
  ![](https://i.imgur.com/muT4BlH.jpg)
</details>

## Albino elephant

Let's create a dummy index to show this error scenario:
`curl -XPUT localhost:9200/albino-elephant`{{execute}}
 
 In Kibana:
 ```
PUT albino-elephant/_doc/1
{
   "title": "albino",
   "body": "elephant"
}
PUT albino-elephant/_doc/2
{
   "title": "elephant",
   "body": "elephant"
}
 ```

Now, if we search for `albino elephant`, which document should score higher if we do a `multi_match` `most_fields` query?

```
GET albino-elephant/_search
{
  "query": {
    "multi_match": {
      "query": "albino elephant",
      "type": "most_fields", 
      "fields": ["title", "body"]
    }
  }
}
```

What happened? Why doesn't `albino elephant` score higher?

For field-centric search, the fields don't interact with each other. The title search is computed independently from the body.

> Signal discordance - the disconnect between the specific fields present in a document schema model and the users' general mental model of the content.

## Tools to solve this issue

### `all` fields
We can group fields together at index time into a single field that contains all the data. An example of this: `cast.name` and `director.name` could be grouped into a `people.name` all-field. This addresses `signal discordance` since users usually don't have a way to tell the search engine which field they want to search on - they are searching for a person's name that is related to the movie.

### `cross_fields` fields

