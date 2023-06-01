from pymilvus import (
    connections,
    utility,
    FieldSchema, CollectionSchema, DataType,
    Collection,
)
import numpy as np
import pandas as pd


connections.connect("default", host="10.200.0.43", port="19530")
print(utility.list_collections())
utility.drop_collection('ctrip_desc_norm_xb0')
print(utility.list_collections())


fields = [
    FieldSchema(name="pk", dtype=DataType.INT64, is_primary=True, auto_id=False,),
    FieldSchema(name="embeddings", dtype=DataType.FLOAT_VECTOR, dim=1024),
    FieldSchema(name="id",dtype=DataType.INT64,)
]
schema = CollectionSchema(fields,)
collection=Collection('ctrip_desc_norm_xb0',schema)
print(utility.list_collections())


with open('/data1/shiba/langchain-ChatGLM/content/full_hotels_conversion/ctrip_desc_norm_xb0.npy',mode='rb') as f:
    xb=np.load(f)
ids_split_df=pd.read_csv('/data1/shiba/langchain-ChatGLM/content/full_hotels_conversion/external_ids_split.csv')
assert xb.shape[0]==ids_split_df.shape[0] and xb.shape[1]==1024
pk_list=[i for i in range(xb.shape[0])]
assert len(pk_list)==xb.shape[0]


def mini_batch_insert2milvus(left_idx:int,right_idx:int,):
    entities=[
        pk_list[left_idx:right_idx],
        xb[left_idx:right_idx,:],
        ids_split_df['id_split'].tolist()[left_idx:right_idx],
    ]
    print(left_idx,right_idx,collection.num_entities)
    insert_result=collection.insert(entities)
    collection.flush()
    print(left_idx, right_idx, collection.num_entities,'\n')


cur_idx=0
step=10000
while cur_idx<len(pk_list):
    mini_batch_insert2milvus(left_idx=cur_idx,right_idx=cur_idx+step,)
    cur_idx+=step
