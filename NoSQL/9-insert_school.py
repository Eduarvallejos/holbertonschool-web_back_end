#!/usr/bin/env python3
"""
This function inserts a school document into a MongoDB collection
"""


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a school document into a MongoDB collection.

    Args:
        mongo_collection(Collection): PyMongo collection object.
            The collection where the school document will be inserted.
        **kwargs: Arbitrary keyword arguments representing the fields and
                    values of the school document.

    Returns:
        pymongo.results.InsertOneResult: The result of the insert operation.
            This includes information about the inserted document,
            such as its ID.
    """
    insert_doc = mongo_collection.insert_one(kwargs).inserted_id

    return insert_doc
