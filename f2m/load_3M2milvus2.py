from pymilvus import (
    connections,
    utility,
    FieldSchema, CollectionSchema, DataType,
    Collection,
)
import numpy as np
import pandas as pd


connections.connect("default", host="10.200.0.43", port="19530")
collection=Collection('ctrip_desc_norm_xb0',)
print(utility.list_collections())
print(collection.num_entities)

index={
    "index_type":'FLAT',
    'metric_type':'IP',
    "params":{},
}
collection.create_index("embeddings",index)
