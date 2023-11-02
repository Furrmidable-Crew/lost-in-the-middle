# Lost In The Middle
 
[![awesome plugin](https://custom-icon-badges.demolab.com/static/v1?label=&message=awesome+plugin&color=F4F4F5&style=for-the-badge&logo=cheshire_cat_black)](https://)

Plugin based on [*Lost in the Middle: How Language Models Use Long Contexts*](https://arxiv.org/abs/2307.03172).

In the paper the authors state that LLMs perform better if the relevant information is at the beginning or end of the context, when there is a greater number of documents than N (N>10 or so). According to this study, it is necessary to reorder the list of documents returned by the retriever for better responses.

The plugin works only on [Declarative Memory](https://cheshire-cat-ai.github.io/docs/conceptual/memory/declarative_memory/) that contains an extract of documents uploaded to the Cat.

> **Important**
> Lost In The Middle is very useful if you get at least more than 10 documents returned from the declarative memory.
> Before using it download and enable the [C.A.T. plugin](https://github.com/Furrmidable-Crew/cat_advanced_tools) from the Plugins store, [follow the instructions](https://github.com/Furrmidable-Crew/cat_advanced_tools#usage) to increase the k parameter of the declarative memory.
