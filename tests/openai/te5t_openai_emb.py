import openai

openai.api_key='sk-chaogeyangjinjiewuyuanqingchenconggejinxiaoluweng'
response = openai.Embedding.create(input=['derby innovation lab','chao yang','jinjie wu'], model="text-embedding-ada-002")
print(response)