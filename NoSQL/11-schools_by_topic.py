#!/usr/bin/env python3
"""
This script contains a function to find schools covering a
specific topic.
"""


def schools_by_topic(mongo_collection, topic):
    """
    Find schools that cover a specific topic.

    Parameters:
        mongo_collection (pymongo.collection.Collection):
            pymongo collection object.
        topic (str): Topic to search for.

    Returns:
        pymongo.cursor.Cursor: Cursor containing documents of
            schools covering the specified topic.
    """
    school_list = mongo_collection.find({"topics": topic})
    return school_list
