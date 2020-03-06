# Lucene/Elasticsearch review 101
1. What is a document in Lucene?
<details>
  <summary>Answer</summary>
  
  - A document is a sequence of Fields;
  - Fields are sequences of Terms;
  - Terms are the basic atomic unit on which we run search.

![alt text](https://i.imgur.com/fTaaDrn.jpg "A conceptual representation of a Lucene document")

    
</details>
<br>

2. What is the core data structure that stores information in Lucene?
<details>
  <summary>Answer</summary>
  
## The inverted index!
- Stores a mapping of `term -> Array<DocID>`;
</details>
<br>

3.  How do we transform free-text into terms?
<details>
  <summary>Answer</summary>
  
## Text analysis
- We run our text through a Text Analysis pipeline. This is internal to Lucene, but Elasticsearch exposes it to us for use and customization.
- Each pipeline can be thought of as:
` text -> Char Filter -> Tokenizer -> [Token filter, Token filter, ...] -> tokens`

![alt text](https://i.imgur.com/hp88Szh.jpg "Text analysis pipeline")

</details>
<br>

4. What are tokens?
<details>
  <summary>Answer</summary>
  
## Tokens
- Terms with additional metadata;
- Tokens are strongly dependent on the tokenizer and the token filters used. For exmaple, the following text:
`The Brown's fiftieth wedding anniversary, at Café Olé`
could be tokenized into (assuming it ran through an ASCII character filter first):
`[The][Brown's][fiftieth][wedding][anniversary][at][Cafe][Ole]`
And if we apply token filters, we could end up with:
`[   ][brown  ][fiftieth][wedding][anniversary][  ][cafe][ole]`
</details>
<br>
