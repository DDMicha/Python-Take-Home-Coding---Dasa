from pymongo import MongoClient
import urllib.parse


username = urllib.parse.quote_plus('root')
password = urllib.parse.quote_plus('passwd1234')

cliente = MongoClient('mongodb://{0}:{1}@localhost:27017/'.format(username, password))

banco = cliente['wikidb']
album = banco['wikimedia']
album = banco.album
print(album.find_one())
print(album.count())
#2777
#1738