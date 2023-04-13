import pandas as pd
import json


with open(file='./ctrip_hotels_details_202108_sanya.csv',mode='r') as f:
    res=f.readlines()

cols=res.pop(0)
incident=[]
for i in range(len(res)):
    temp_str=res[i]
    hotel_id= temp_str.split(',')[0]
    if not  hotel_id.isnumeric():
        incident.append((i,temp_str))

# which hotel id is 'wrong'
# 70304985 , 78059891 both @ address col
df=pd.read_csv('ctrip_hotels_details_202108_sanya.csv',
               na_filter=False,
               #dtype='string',
               )
incident_df=df[df['hotel_id'].isin([70304985,78059891,]) ]






# desc
def apply_fn4ext_hotel_id_desc(sz:pd.Series):
    temp={
        'id':sz['hotel_id'],
        'text':sz['description'],
    }
    return pd.Series(temp)


out_df=df.apply(func=apply_fn4ext_hotel_id_desc,
                axis=1,
                )
out_list=[]
for i in range(out_df.shape[0]):
    out_list.append(
        {
            'id':str(out_df.iloc[i]['id']),
            'text':out_df.iloc[i]['text'],
        }
    )

with open(file='./sanya_desc.json',mode='w') as f:
    f.write(
        json.dumps(
            out_list,
            ensure_ascii=False,
            indent=3,
        )
    )





# coordinate
def apply_fn4hotel_id_coord_ext(sz:pd.Series):
    temp={
        'id':sz['hotel_id'],
        'lat_gd':sz['lat_gd'],
        'lng_gd':sz['lng_gd'],
    }
    return pd.Series(temp)


out_df:pd.DataFrame=df.apply(func=apply_fn4hotel_id_coord_ext,
                axis=1,
                )

out_df.to_csv('sanya_coord.csv',sep='\x01',header=True,index=False,)

