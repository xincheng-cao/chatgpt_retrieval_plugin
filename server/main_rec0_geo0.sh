#!/bin/bash


export DATASTORE=milvus

export BEARER_TOKEN=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2ODA1OTM4MTUsImRpY3RhdG9yIjoiaW5ub3ZhdGlvbl9sYWIifQ.WkxFZf7xoIRICs4D8dsbR35rr6OwUatx0HVULKTd61Y

export OPENAI_API_KEY=sk-chaogejinjieyuanqingconggexiaolu

export PYTHONPATH=/data1/shiba/chatgpt_retrieval_plugin

cd /data1/shiba/chatgpt_retrieval_plugin && \
nohup \
  /data1/shiba/chatgpt_retrieval_plugin/.venv/bin/python server/main_rec0_geo0.py \
  > server/main_rec0_geo0.out \
  2> server/main_rec0_geo0.err &