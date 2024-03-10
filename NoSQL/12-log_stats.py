#!/usr/bin/env python3
"""Log stats from collection"""

from pymongo import MongoClient

METHODS = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']

def log_stats(mongo_collection):
    """Script that provides some stats about Nginx logs stored in MongoDB"""
    # Conteo total de logs
    total_logs = mongo_collection.count_documents({})
    print(f'{total_logs} logs')
    print('Methods:')

    # Conteo y impresión de documentos para cada método
    for method in METHODS:
        count = mongo_collection.count_documents({'method': method})
        print(f'\tmethod {method}: {count}')

    # Conteo e impresión del número de chequeos de estado
    status_check = mongo_collection.count_documents({'path': '/status'})
    print(f'{status_check} status check')

if __name__ == "__main__":
    # Conexión a MongoDB
    client = MongoClient('mongodb://127.0.0.1:27017/')
    nginx_collection = client.logs.nginx
    log_stats(nginx_collection)
    