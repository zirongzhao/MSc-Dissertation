#Combine many csv
import pandas as pd
import glob

path = r'C:\Users\40587\Desktop\ng_data' # use your path
all_files = glob.glob(path + "/*.csv")

li = []
len(li)

for filename in all_files:
    df = pd.read_csv(filename, index_col=None, header=0,
    names=['user_id_ref','user_id','user_name','tweet_id','time','tweet_text','user_loc','user_des','lang'],
    dtype={'user_id_ref': str, 'user_id': str, 'user_name': str, 'tweet_id': str, 'time': str,
           'tweet_text': str, 'user_loc': str, 'user_des': str, 'lang':str},
    )
    li.append(df)

df_ng = pd.concat(li, axis=0, ignore_index=True)
df_ng.head()
len(df_ng['tweet_id'])

df_ng['user_id'].nunique()

df_ng.drop('lang', axis=1, inplace=True)

df_ng['tweet_id'].head()

len(df_ng)

df_ng.to_csv('df_ng.csv',index=False)