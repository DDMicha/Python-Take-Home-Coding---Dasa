import requests
import json
from elasticsearch import Elasticsearch
es = Elasticsearch([{'host': 'elasticsearch', 'port': 9200}])

s = requests.Session()

def write_mongo(data_dict):
  try:
    data_id = es.index(index="wiki", doc_type='wiki', body=data_dict)
    print(data_id)
  except Exception as exception:
    print(exception)  

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

read_stream()
