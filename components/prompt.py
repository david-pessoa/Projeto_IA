def extract_metadata(chunk):
    file = chunk.metadata["document"]
    page = chunk.metadata["page"]
    pos = chunk.metadata["position"]
    return file, page, pos

def results_template(results):
    results_sorted = sorted(results, key=extract_metadata)
    return results_sorted
'''
def input_template(query, results):
    context = "\n".join([results['documents'][0][i] for i in results['documents'][0]])
    augment_prompt = f"""
    Use o contexto abaixo para responder à pergunta.

    Contexto:
    {context}

    Pergunta: {query}
    """

    return augment_prompt
'''