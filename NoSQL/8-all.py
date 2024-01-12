#!/usr/bin/env python3
""" list all """


def list_all(mongo_collection):
    """ list all """
    lista = []
    for ob in mongo_collection.find():
        lista.append(ob)
    return lista
