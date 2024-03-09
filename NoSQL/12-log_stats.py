#!/usr/bin/env python3
"""Mongodb"""
from pymongo import MongoClient


if __name__ == "__main__":

    client = MongoClient("mongodb://127.0.0.1:27017")
    coll = client.logs.nginx

    method = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    print(f"{coll.count_documents({})} logs")
    print("Methods:")

    for m in method:
        print(f"\tmethod {m}: {coll.count_documents({'method': m})}")

    print(str(coll.count_documents({"method": "GET", "path": "/status"}))\
            + " status check")
