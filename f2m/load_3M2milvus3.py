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

collection.load()
print('done loading')
def query_10(collection:Collection):
    output_fields=[e.name for e in collection.schema.fields]

    res=collection.query(
        expr='pk<10',
        output_fields=output_fields,
    )
    def get_key_fn(e):
        return e['pk']
    res.sort(reverse=False,key=get_key_fn)
    return res
res=query_10(collection)
print('done')