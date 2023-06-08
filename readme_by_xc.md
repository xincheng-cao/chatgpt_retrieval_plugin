## poetry 2 requirements 2 pipenv
poetry2reqs.py

## Milvus
refer: https://milvus.io/docs/v2.0.x/install_standalone-docker.md

cd milvus_standalone

wget https://github.com/milvus-io/milvus/releases/download/v2.0.2/milvus-standalone-docker-compose.yml -O docker-compose.yml

sudo docker-compose up -d

sudo docker-compose ps

pytest ./tests/datastore/providers/milvus/test_milvus_datastore.py (run in pycharm, test not working!)

sudo docker-compose down

sudo rm -rf  volumes

## Milvus run test
cd examples/docker/milvus

sudo docker-compose up -d

sudo docker ps

pytest ./tests/datastore/providers/milvus/test_milvus_datastore.py (run in pycharm, test working)

## env variable
@ confs/gen_env_vars.py

## start server
@ server/main.py (use pycharm to run, not poetry run start)

## https://platform.openai.com/docs/guides/embeddings


### texts2embs
![](pics/embeding_output_dim_size.png)

### euclidean dist vs cos sim vs dot prod vs l2 norm
![](pics/l2_vs_cosine.png)





### configure Milvus
refer to: https://milvus.io/docs/configure-docker.md
https://juejin.cn/post/6966524585458171940


cd examples/docker/milvus

wget https://raw.githubusercontent.com/milvus-io/milvus/v2.2.5/configs/milvus.yaml

![](pics/Configure-Milvus-with-Docker-Compose-Milvus-documentation.png)



## updated on Jun 8th,2023
### desc
- The repo I cloned from the official OpenAI repository located at https://github.com/openai/chatgpt-retrieval-plugin, commit ID 15b1169. It hasn't been updated to the latest version.
- I made some modifications based on the official OpenAI repo and used Milvus DB as the backend vector database.
- Then I added certain static information from Ctrip as input to Milvus.
- This service is essentially a RESTful API for querying the vector database.
### steps
0. scripts/process_json/convert_csv2json.py: data pre-processing (to all kinds of jsons and coord csv)
1. readme_by_xc.md: how to deploy milvus
2. scripts/process_json/process_json_rec0.py: upsert to milvus (all the jsons like "sanya_foooooo.json" @ scripts/process_json/ are upsert to collection ctrip_hotel_cols_4_rec0. edit parameters: --filepath)
3. server/main_rec0_geo0.sh: start restful api service
4. server/te5t_rec0_geo0_0.py: how to test api service
5. server/te5t_rec0_geo0_0.ipynb: how to interact w/ milvus use pymilvus ( and insert scripts/process_json/sanya_coord.csv use pymilvus directly to collection ctrip_hotel_cols_4_geo0)
6. f2m/: the data is actually from another repo (https://github.com/xincheng-cao/langchain-ChatGLM) which uses faiss. and the scripts insert the vector(~3M,1024) into milvus

