from requests import get,post
from dotenv import load_dotenv
import os
import base64
import json
import pandas as pd

load_dotenv()

client_id= os.getenv('client_id')
client_secret= os.getenv('client_secret')
redirect_url = 'http://localhost:8888/callback'


    
def get_token():
    auth_string= client_id + ":" + client_secret
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = base64.b64encode(auth_bytes).decode("utf-8")

    url= "https://accounts.spotify.com/api/token?"
    headers= {"Authorization": "Basic " + auth_base64,
              "Content-type": "application/x-www-form-urlencoded"
    }
    
    data = {"grant_type": "client_credentials"}
    result = post(url,headers=headers,data=data)
    json_result=json.loads(result.content)
    token= json_result["access_token"]
    return token


def get_auth_header(token):
    return {"Authorization": "Bearer " + token}


user_id='7asAr33Uw7KASjyl0RJ4Eb'

def playlist(token,user_id):
    query_url=f"https://api.spotify.com/v1/users/"+user_id+"/playlists"
    headers= get_auth_header(token)
    result= get(query_url,headers=headers)
    json_result= json.loads(result.content)
    print(json_result)



def myplaylist(token):
    myurl="https://api.spotify.com/v1/users/fnnlbzrvjex6r6tgmdx6cr4xq/playlists"
    headers= get_auth_header(token)
    myresult= get(myurl,headers=headers)
    result=myresult.json()
    return result
    # json_results= json.loads(myresult.content)
    # print (json_results)

token= get_token()

test=myplaylist(token)

a=[]
for i in test['items']:
    a.append(i)


test = pd.DataFrame(a)
print(test)