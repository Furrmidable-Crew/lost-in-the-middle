from cat.mad_hatter.decorators import hook

def litm(documents):
    """
    Function based on Haystack's LITM ranker:
    https://github.com/deepset-ai/haystack/blob/main/haystack/nodes/ranker/lost_in_the_middle.py

    Lost In The Middle is based on the paper https://arxiv.org/abs/2307.03172
    Check it for mor details.


    Parameters
    ----------
    documents: List of documents (the declarative working memories)

    Returns
    ----------
    litm_docs: The same list but reordered
    """
    if len(documents) == 1:
        return documents
    
    document_index = list(range(len(documents)))
    lost_in_the_middle_indices = [0]

    for doc_idx in document_index[1:]:
        insertion_index = len(lost_in_the_middle_indices) // 2 + len(lost_in_the_middle_indices) % 2
        lost_in_the_middle_indices.insert(insertion_index, doc_idx)
        litm_docs = [documents[idx] for idx in lost_in_the_middle_indices]
    return litm_docs


@hook(priority=1)
def after_cat_recalls_memories(cat) -> None:
    """Hook after semantic search in memories.

    The hook is executed just after the Cat searches for the meaningful context in memories
    and stores it in the *Working Memory*.

    Parameters
    ----------
    cat : CheshireCat
        Cheshire Cat instance.

    """
    if cat.working_memory['declarative_memories']:
        litm_docs = litm(cat.working_memory['declarative_memories'])
        cat.working_memory['declarative_memories'] = litm_docs
    else:
        print("#HicSuntGattones")
    pass # do nothing
