# Search explained
We saw that the Boolean model is what finds a list of matching documents, but how does Lucene know how to order them?

The relevance of a document is determined by the _weight_ of each query term that appears in that document. This _weight_ is, in turn, determined by: `TF x IDF`.

# Term frequency (`TF`)
> How often does the term appear in the document?

If a term occurs more times in a document, it's probably more relevant for that term.


# Inverse Document frequency (`IDF`)
> How often does the term appear in all documents in the corpus?

If a term is present in many documents, it's not that relevant of a term. This means that rare words will have a really high `IDF`, while really common words have low `IDF` values.

# Putting things together

From a high-level overview, you will see the following pattern again and again when you `explain` a query:
```
weight(field:term in docID) [PerFieldSimilarity]:  score 
result of:
    fieldWeight in docID                           score
    product of:
        tf(freq=1.0), with freq of 1:              tf 
        idf(docFreq=1, maxDocs=1):                 idf
        boosts                                     boost
```
This is straight-forward for a search on a single term, but to combine multiple terms, a concept known as the vector space model is used.

# Vector space model*

> Disclaimer: Okapi BM25 has a different way of calculating multi-field scores, but the vector space model is a good conceptual tool to help illustrate the ideas.

Imagine a multi-term query like `happy hippopotamus`. We can look up the weights for each term, and lets say `happy=2`, `hippopotamus=5`. The multi-term query can be thought of as a vector: `[2,5]`.

![](https://www.elastic.co/guide/en/elasticsearch/guide/2.x/images/elas_17in01.png)

Assuming we have the following documents:
```
1. I am happy in summer.
2. After Christmas I’m a hippopotamus.
3. The happy hippopotamus helped Harry.
```
We can generate the following vectors for these:
```
1. [2, 0]
2. [0, 5]
3. [2, 5]
```
A visual representation of this on a 2D graph would be:
![](https://www.elastic.co/guide/en/elasticsearch/guide/2.x/images/elas_17in02.png)


The actual vectors are multi-dimensional vectors, and calculating the similarity between the query terms and the document terms is a matter of using the dot product between the query vector and the document vector.

---
<details>
  <summary>For those not afraid of math</summary>

  Okapi BM25 uses the following formula to calculate the TFxIDF of a document:

  ![](https://wikimedia.org/api/rest_v1/media/math/render/svg/43e5c609557364f7836b6b2f4cd8ea41deb86a96)

    For the most part, this is opaque to the developer and there is rarely any reason to go in and start tuning the individual parameters of the algorithm. 
</details>
<br>


Credits: Elasticsearch The Definitive Guide