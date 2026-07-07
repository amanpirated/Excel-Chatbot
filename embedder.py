from FlagEmbedding import BGEM3FlagModel

class Embedder:
    def __init__(self):
        self.model = BGEM3FlagModel(
            "BAAI/bge-m3",
            use_fp16=False
        )
    def generate_embeddings(self, chunks):
        # Collect all texts
        texts = []
        for chunk in chunks:
            texts.append(chunk["text"])
        # Generate embeddings for ALL texts at once
        embeddings = self.model.encode(
            texts,
            return_dense=True,
            return_sparse=True,
            return_colbert_vecs=True
        )
        # Attach embeddings to each chunk
        for i, chunk in enumerate(chunks):
            chunk["dense"] = embeddings["dense_vecs"][i]
            chunk["sparse"] = embeddings["lexical_weights"][i]
            chunk["colbert"] = embeddings["colbert_vecs"][i]
        return chunks