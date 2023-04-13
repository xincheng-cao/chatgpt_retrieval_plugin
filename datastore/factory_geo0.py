#from datastore.datastore import DataStore
from datastore.datastore_geo0 import DataStore
import os


async def get_datastore() -> DataStore:
    datastore = os.environ.get("DATASTORE")
    assert datastore is not None

    match datastore:
        case "llama":
            from datastore.providers.llama_datastore import LlamaDataStore
            return LlamaDataStore()

        case "pinecone":
            from datastore.providers.pinecone_datastore import PineconeDataStore

            return PineconeDataStore()
        case "weaviate":
            from datastore.providers.weaviate_datastore import WeaviateDataStore

            return WeaviateDataStore()
        case "milvus":
            import datastore.providers.milvus_datastore_geo0 as milvus_datastore_geo0

            return milvus_datastore_geo0.MilvusDataStore()
        case "zilliz":
            from datastore.providers.zilliz_datastore import ZillizDataStore

            return ZillizDataStore()
        case "redis":
            from datastore.providers.redis_datastore import RedisDataStore

            return await RedisDataStore.init()
        case "qdrant":
            from datastore.providers.qdrant_datastore import QdrantDataStore

            return QdrantDataStore()
        case _:
            raise ValueError(f"Unsupported vector database: {datastore}")
