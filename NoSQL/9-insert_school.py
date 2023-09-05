#!/usr/bin/env python3
"""
Script inserts a new document in a collection
"""


def insert_school(mongo_collection, **kwargs):
    """
    Insert a document in Python
    """
    if mongo_collection is None:
        return None
    return mongo_collection.insert_one(kwargs).inserted_id
