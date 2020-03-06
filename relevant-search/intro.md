This interactive course is intended to demystify some of the quirks of Elasticsearch and Lucene.

Specifically, we will go over:
1. What is relevance? Who's problem is relevance?
2. Boolean queries and basic Lucene search operations.
    - This section is intended to describe the building blocks of search, as well as show you how to use the Elasticsearch `_validate` API to check the Lucene query that gets executed.
3. Debugging relevance
    - This section explains why your search might be returning irrelevant results. We'll go over the `_explain` API in Elasticsearch to understand why the 
4. Tokenize
    - Precision vs. Recall. Why tokens matter and how we can tweak our analysis to increase fight the precision v. recall dilemma.
5. Multifield search (Field-centric search)
    - Introduces query strategies that help us in searching across multiple fields;
6. Term-centric search
    - More query strategies, this time focused on the users' basic understanding of relevance.
7. Custom boosting and scoring
