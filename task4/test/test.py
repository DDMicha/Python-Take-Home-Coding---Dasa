from elasticsearch import Elasticsearch

es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

res = es.search(index="wiki", body={"query": {"match_all": {}}})

print(res)