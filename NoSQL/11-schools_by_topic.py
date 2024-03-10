#!/usr/bin/env python3
""" schools by topic """



def schools_by_topic(mongo_collection, topic):
    """ schools by topic """
    res = []
    for ob in mongo_collection.find({"topics": topic}):
        res.append(ob)
    return res
