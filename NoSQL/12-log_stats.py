#!/usr/bin/env python3
""" log stats """


from pymongo import MongoClient

if __name__ == '__main__':
    client = MongoClient('mongodb://localhost')
    dataB = client['logs']
    collect = dataB['nginx']
    print(f"{collect.count_documents({})} logs")
    print('Methods:')
    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    for method in methods:
        print(f"\tmethod {method}: {collect.count_documents({'method': method})}")
    message = 'status check'
    print(f"{collect.count_documents({'method': 'GET', 'path': '/status'})} {message}")
