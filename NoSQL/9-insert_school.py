#!/usr/bin/env python3
""" insert school """



def insert_school(mongo_collection, **kwargs):
    """ insert shool """
    res = mongo_collection.insert_one(kwargs)
    return res.inserted_id
