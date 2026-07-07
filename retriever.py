from FlagEmbedding import BGEM3FlagModel
class Retriever:

    def __init__(self, vectordb):
        self.db = vectordb
        self.model = BGEM3FlagModel(
            "BAAI/bge-m3",
            use_fp16=False
        )
    def embed_query(self, query):

        embedding = self.model.encode(
            [query],
            return_dense=True,
            return_sparse=False,
            return_colbert_vecs=False
        )
        return embedding["dense_vecs"][0]

    def retrieve(self, query, top_k=3):
        query_vector = self.embed_query(query)
        results = self.db.client.query_points(
            collection_name=self.db.collection_name,
            query=query_vector.tolist(),
            limit=top_k
        )
        contexts = []
        for point in results.points:
            contexts.append(point.payload["text"])
        return contexts
    