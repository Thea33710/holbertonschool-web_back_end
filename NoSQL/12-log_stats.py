#!/usr/bin/env python3
"""
This module had a function that provides
some stats about Nginx logs stored in MongoDB.
"""
from pymongo import MongoClient


def log_stats(mongo_collection):
    """
    Provides some stats about Nginx logs stored in MongoDB.
    """
    total_logs = mongo_collection.count_documents({})

    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    method_counts = {}
    for method in methods:
        method_counts[method] = mongo_collection.count_documents(
            {"method": method}
        )

    status_200_count = mongo_collection.count_documents(
        {"status": 200}
    )

    print(f"{total_logs} logs")
    print("Methods:")
    for method in methods:
        print(f"\tmethod {method}: {method_counts[method]}")
    print(f"{status_200_count} status check")
