#!/usr/bin/env python3
"""
This function lists all the documents in a MongoDB collection
"""


def list_all(mongo_collection):
    """
    Lists all the documents in a MongoDB collection.

    Args:
        mongo_collection(Collection): PyMongo collection object.
            MongoDB collection from which documents will be listed.

    Returns:
        List[Dict[str, Any]]: A list of documents from the received collection.
            A list of dictionaries representing the documents in the collection
    """

    documents = []
    cursor = mongo_collection.find()

    for document in cursor:
        documents.append(document)

    return documents
