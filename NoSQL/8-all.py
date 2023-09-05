#!/usr/bin/env python3
"""
Script lists all documents in a collection
"""


def list_all(mongo_collection):
    """
    List all documents in Python
    """
    if mongo_collection is None:
        return []
    return mongo_collection.find()
