import requests


temp_json={
    'queries':[
        {
            'query':'喜欢花朵,喜欢别墅',
            'top_k':10,
        },
        {
            'query': '喜欢花朵,喜欢别墅',
            'top_k': 10,
            'filter':{
                'document_id':'in ["43429526","77186305","2606364","48030520","77157804",]',
            }
        },
        {
            'query': '喜欢花朵,喜欢别墅',
            'top_k': 10,
            'filter': {
                'document_id': 'in ["48030520",]',
            }
        },
    ]
}
BEARER_TOKEN='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2ODA1OTM4MTUsImRpY3RhdG9yIjoiaW5ub3ZhdGlvbl9sYWIifQ.WkxFZf7xoIRICs4D8dsbR35rr6OwUatx0HVULKTd61Y'
res=requests.post(
    url='http://10.200.0.43:13000/query_rec0',
    json=temp_json,
    headers = {
        "Content-Type": "application/json",
        'Authorization':'Bearer '+BEARER_TOKEN,
    }
)
resp=res.json()




temp_json={
    'queries':[
        {
            'query':'[18.375606327240487,109.7312463076794]',
            'top_k':10,
        },
        {
            'query': '[18.23683982786473,109.37310133493273]',
            'top_k': 10,
        },
    ]
}
BEARER_TOKEN='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2ODA1OTM4MTUsImRpY3RhdG9yIjoiaW5ub3ZhdGlvbl9sYWIifQ.WkxFZf7xoIRICs4D8dsbR35rr6OwUatx0HVULKTd61Y'
res=requests.post(
    url='http://10.200.0.43:13000/query_geo0',
    json=temp_json,
    headers = {
        "Content-Type": "application/json",
        'Authorization':'Bearer '+BEARER_TOKEN,
    }
)
resp=res.json()



print('done')
