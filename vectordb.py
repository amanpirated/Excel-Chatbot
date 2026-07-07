from qdrant_client import QdrantClient
from qdrant_client.models import (
    Distance,
    VectorParams,
    PointStruct
)

class VectorDB:
    def __init__(self):
        self.client = QdrantClient(":memory:")
        self.collection_name = "employee_data"

    def create_collection(self):
        self.client.create_collection(
            collection_name=self.collection_name,
            vectors_config=VectorParams(
                size=1024,
                distance=Distance.COSINE
    )
)
    def insert_chunks(self, chunks):
        points = []
        for i, chunk in enumerate(chunks):
            point = PointStruct(
                id=i,
                vector=chunk["dense"],
                payload={
                    "text": chunk["text"],
                    "metadata": chunk["metadata"]
                }
            )
            points.append(point)

        self.client.upsert(
            collection_name=self.collection_name,
            points=points
        )