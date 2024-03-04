#!/usr/bin/env python3
"""Connect to MongoDB and retrieve statistics about Nginx logs"""
from pymongo import MongoClient


if __name__ == "__main__":
    """Connect to MongoDB"""
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client['logs']
    collection = db['nginx']

    """Count total number of documents in collection"""
    total_doc = collection.count_documents({})
    """Count number of documents with method=GET and path=/status"""
    status_count = collection.count_documents(
        {"method": "GET", "path": "/status"})

    """Count number of documents for each HTTP method"""
    methods = [
        {"method": "GET"},
        {"method": "POST"},
        {"method": "PUT"},
        {"method": "PATCH"},
        {"method": "DELETE"},
    ]
    totales = [collection.count_documents(method) for method in methods]


    print(f'{total_doc} logs')
    print('Methods:')
    for i, t in enumerate(totales):
        print(f'\tmethod {methods[i].get("method")}: {t}')
    print(f'{status_count} status check')
