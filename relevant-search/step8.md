# Multifield search

Elasticsearch and Lucene have 2 flavors of multi-field search:
- <b>field-centric</b> - the search runs against each specified field in isolation. The results are then combined to produce the score;
- <b>term-centric</b> - Each field is searched on a term-by-term basis. This produces a per-term score that combines the influence from each field on the specific term;