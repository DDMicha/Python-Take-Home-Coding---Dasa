import requests
import json
from pymongo import MongoClient
import urllib.parse


username = urllib.parse.quote_plus('root')
password = urllib.parse.quote_plus('passwd1234')
client = MongoClient('mongodb://{0}:{1}@mongo:27017/'.format(username, password))

banco = client['wikidb']
collection = banco['wikimedia']
collection = banco.album

s = requests.Session()

def write_mongo(data_dict):
  try:
    data_id = collection.insert_one(data_dict).inserted_id
    print(data_id)
  except NameError:
    print(NameError)  

def streaming():
    #get funciton api wikimedia
    req = requests.Request("GET",'https://stream.wikimedia.org/v2/stream/recentchange').prepare()
    
    resp = s.send(req, stream=True)

    for line in resp.iter_lines():
        if line:
            yield str(line, 'utf-8')


def read_stream():

    for line in streaming():
        if line.startswith('data'):
          data_dict = json.loads(line[6:])
          # only show non-bot
          if data_dict['bot'] == False:
            write_mongo(data_dict)
            # print (data_dict)
            #  data_id = collection.insert_one(data_dict).inserted_id
            #  print(data_id)


read_stream()