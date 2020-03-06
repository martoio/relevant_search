# Multifield search

Elasticsearch and Lucene have 2 flavors of multi-field search:
- <b>field-centric</b> - the search runs against each specified field in isolation. The results are then combined to produce the score;
- <b>term-centric</b> - Each field is searched on a term-by-term basis. This produces a per-term score that combines the influence from each field on the specific term;

# Field-centric
<details>
    <summary>Illustration</summary>

  ![](https://i.imgur.com/d3yStsX.jpg)
</details>

Process:
- Elasticsearch `multi_match` query;
- For each field, run a query-time analysis (pass the query through the text analysis pipeline) to produce tokens;
- Perform Boolean search on the tokens with each token as a `SHOULD` clause;
- Produce a score for each field;
- Combine the fields using a ranking function;

The ranking function used depends on the `type` of `multi_match` query we use. The two main forms are:

- `best_fields` (default) - take the highest scoring field. In the illustration, repalce `fn` with `max`;
    - <code>score = s<sub>title</sub> + tie_breaker * (s<sub>overview</sub> + s<sub>field_1</sub> + s<sub>field_2</sub> ...  + s<sub>field_n</sub>)</code>
    - Useful when multiple fields are not likely to match the search string.
    - Essentially we can have a search that determines "The user must be searching for a title".
- `most_fields` - Sum of field scores multiplied by a _coordinating factor_;
    - <code>score = (s<sub>title</sub> + s<sub>overview</sub> + s<sub>field_1</sub> + s<sub>field_2</sub> ...  + s<sub>field_n</sub>) * coord</code>, where <code>coord = # matching clauses / number of total clauses</code>
    - Useful when multiple fields could match the search string;
    - Essentially we can have a search that says "The ideal document matches a document's title, some part of the overview, some part of the director's name, etc."

### Testing it out
```
GET /tmdb/_search
{
    "query": {
        "multi_match": {
            "query": "aliens michael jordan",
            "fields": ["title", "overview", "cast.name", "directors.name"],
            "type": "best_fields"
        }
    }
}
```
