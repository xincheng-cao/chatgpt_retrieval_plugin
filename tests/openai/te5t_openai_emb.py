import openai

openai.api_key='sk-chaogeyangjinjiewuyuanqingchenconggejinxiaoluweng'
response = openai.Embedding.create(input='derby innovation lab', model="text-embedding-ada-002")
print(response)