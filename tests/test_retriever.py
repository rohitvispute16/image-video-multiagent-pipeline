from rag.retriever import get_retriever


def test_retriever():

    retriever = get_retriever()

    docs = retriever.invoke("cinematic wedding")

    assert docs is not None
    assert len(docs) > 0