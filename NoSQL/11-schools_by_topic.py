#!/usr/bin/env python3
"""
Script lists all documents in a collection
"""


def schools_by_topic(mongo_collection, topic):
    """
    List all documents in Python
    """
    if mongo_collection is None:
        return []
    return mongo_collection.find({"topics": topic})
