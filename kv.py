import hashlib
import os

def put(key, value):
    h = hash(key)
    if os.path.isfile(os.path.join("/tmp", hash(key))): return None 
    with open(os.path.join("/tmp", h), "wb+") as bin:
        bin.write(value.encode("utf-8"))
    return h

def get(key):
    with open(os.path.join("/tmp", hash(key)), "rb") as bin:
        return bin.read()

def hash(key: str):
    h = hashlib.new('sha256')
    h.update(str.encode(key))
    return h.hexdigest()



