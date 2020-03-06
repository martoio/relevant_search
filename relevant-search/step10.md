# Debugging
- The `_validate/query?explain` gives you the Lucene query that is being run.
- Adding `"explain" true` to the query will make Elasticsearch give you the math it does. This is useful when you aren't sure why particular documents match higher.
- Each field score lives in a "separate universe". This means that scores between fields cannot be directly compared in any meaningful way. Boosting plays a big role here to supress or strengthen certain fields.
- There are different styles of multi-field search. Picking the appropriate search type matters, but it's important to know why and when you would like to use different search types.
- Tokens are the best way to shape your data the way that the user understands it. Tokens should extract the _meaning_ of a document, rather than just the _text_.