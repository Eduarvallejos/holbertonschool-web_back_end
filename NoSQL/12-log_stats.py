#!/usr/bin/env python3
"""Connect to MongoDB and retrieve statistics about Nginx logs"""
from pymongo import MongoClient


if __name__ == "__main__":
    """Connect to MongoDB"""
    client = MongoClient("mongodb://127.0.0.1:27017")
    database = client["logs"]
    collection = database["nginx"]

    """Count total number of documents in collection"""
    total_doc = collection.count_documents({})

    """Count number of documents for each HTTP method"""
    methods = [
        "GET",
        "POST",
        "PUT",
        "PATCH",
        "DELETE"
        ]
    method_stats = {}
    for method in methods:
        method_count = collection.count_documents({"method": method})
        method_stats[method] = method_count

    """Count number of documents with method=GET and path=/status"""
    status_count = collection.count_documents(
        {"method": "GET", "path": "/status"})

    print(f"{total_doc} logs")
    print("Methods:")
    for method, count in method_stats.items():
        print(f"\tmethod {method}: {count}")
    print(f"{status_count} status check")
