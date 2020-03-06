# Lucene Query Syntax
Imagine you have a single search term `dogs`. Given an inverted index, how do you find all documents that match?
<details>
  <summary>Answer</summary>
  
  - Simply look up the term `dogs` in the inverted index and return the array of documents. (known as the "Postings list")
</details>
<br>

That's great, but usually your users would search for more than a single word at a time. How would you parse the query then? For example: `fluffy dogs`

## Boolean queries
Boolean queries combine the results of multiple queries. For example `"fluffy" AND "dogs"`, or `"fluffy" OR "dogs"`.
Boolean queries provide 3 types of filters: `AND`, `OR`, `NOT`.

###   How does it work?
- `AND` - the intersection of the two postings;
- `OR` - the union of the two postings;
- `NOT` - returns an array of documents _between_ the IDs from every posting;
<details>
  <summary>You can think of it as the following python code:</summary>

    ```python
    def AND(postings_term_1, postings_term_2):
        term_1_doc = postings_term_1.next()
        term_2_doc = postrings_term_2.next()

        matches = []
        while term_1_doc != None and term_2_doc != None:
            if term_1_doc == term_2_doc:
                matches.append(term_1_doc)
                term_1_doc = term_1_doc.next()
                term_2_doc = term_2_doc.next()
            elif term_1_doc < term_2_doc:
                term_1_doc = term_1_doc.next()
            else:
                term_2_doc = term_2_doc.next()
        
        return matches
    ```
</details>
<br>

The inputs and outputs of each operation are lists of DocIDs, so we can compose Boolean queries however we choose.

## Lucene `BooleanQuery`
Lucene uses a slightly different syntax. Instead of `AND`, `OR`, and `NOT`, Lucene has `SHOULD`, `MUST` and `MUST_NOT`

- `SHOULD` - might or might not have a match in a given document. BUT the documents that match are ranked higher than those that don't.
- `MUST` - the query has to have a match with a given document, otherwise no match.
- `MUST_NOT` - any document matching this clause is considered not a match. The document is discarded even if it matches a `MUST` or a `SHOULD` clause otherwise.

## Lucene query syntax
Internally, Lucene uses a special syntax to represent queries. Each of the 3 clauses has a special prefix to represent it.

- `MUST` - `+`
- `MUST_NOT` - `-`
- `SHOULD` - no prefix

Here's an example: <br>
`fluffy +dog -rabbit`
<br>
This translates to:
I'm looking for any documenent that `SHOULD` contain fluffy, `MUST` contain `dog`, `MUST_NOT` contain `rabbit`.

Now consider these 3 documents:
`(a) my dog is a fluffy cloud`
`(b) fluffy dogs are better than a fluffy rabbit`
`(c) dogs are cool`

`(b)` contains the term `rabbit` => we discard it.
`(a) and (c)` contain dogs, so they are a match. But `(a)` contains the optional term `fluffy`, so it will rank higher in our search results.

<details>
  <summary>Why don't we use AND, OR, NOT in Lucene?</summary>

  The previous Lucene query would look like this if we used a standard Boolean query: <br>

  `(dog OR (fluffy AND dog)) AND NOT rabbit`

  More verbose and does not allow for "fuzzy" semantics.
</details>
<br>

<details>
  <summary>What about phrases?</summary>

  You've probably seen this one at some point in your life! (and someone has told you that this is how you should be doing all of your searches): <br>
  Lucene phrase search:
  `"fluffy dogs"`

  Internally, Lucene fetches the postings for each term in 1 pass. In the second pass, it removes documents where the terms are not adjecent ()
</details>
<br>
