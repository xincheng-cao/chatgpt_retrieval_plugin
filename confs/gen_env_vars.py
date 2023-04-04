import jwt
from datetime import datetime,timedelta
from pytz import timezone
import time


bearer_token=jwt.encode(
    payload={
        "exp":datetime.now(tz=timezone('asia/shanghai'))+timedelta(seconds=10),
        "dictator":'innovation_lab',
    },
    key='chao',
    algorithm='HS256',
)
print(bearer_token)

time.sleep(9)

ans=jwt.decode(
    jwt=bearer_token,
    key='chao',
    algorithms='HS256',
)
print(ans)


'''
export DATASTORE=milvus
export BEARER_TOKEN=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2ODA1OTM4MTUsImRpY3RhdG9yIjoiaW5ub3ZhdGlvbl9sYWIifQ.WkxFZf7xoIRICs4D8dsbR35rr6OwUatx0HVULKTd61Y
export OPENAI_API_KEY=sk-chaogejinjieyuanqingconggexiaolu
'''