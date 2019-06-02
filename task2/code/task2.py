import requests
import json

s = requests.Session()

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
            print(json.dumps(data_dict, indent = 4, sort_keys=True))


read_stream()

