#!/usr/bin/env python3
"""
Script changes all topics of a school document based on the name
"""


def update_topics(mongo_collection, name, topics):
    """
    Update a document in Python
    """
    if mongo_collection is None:
        return None
    return mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}}).modified_count
