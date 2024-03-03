#!/usr/bin/env python3
"""
This script changes all topics in a school document based on name.
"""


def update_topics(mongo_collection, name, topics):
    """
    Update the topics for all documents matching the school name.

    Parameters:
        mongo_collection (pymongo.collection.Collection):
            pymongo collection object.
        name (str): Name of the school whose topics to update.
        topics (list): List of strings representing the topics approached
            in the school.
    """
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
        )
