#!/usr/bin/env python3
""" MongoDB """
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient()
    nginx_logs = client.logs.nginx

    nums_of_docs = nginx_logs.count_documents({})
    print(f"{nums_of_docs} logs")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        methods_count = nginx_logs.count_documents({"method": method})
        print(f"\t method {method}: {methods_count"}
    status = nginx_logs.count_documnets({"method": "GET", "path": "/status"})
    print(f"{status} status check")
