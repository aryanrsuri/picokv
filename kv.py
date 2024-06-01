import hashlib
import os

def put(key: str, value: str):
    h = hash(key)
    # if os.path.isfile(os.path.join("/tmp", hash(key))): return None 
    with open(os.path.join("/tmp", h), "ab+") as bin:
        bin.write(value.encode("utf-8"))
    return h

def get(key: str):
    try:
        with open(os.path.join("/tmp", hash(key)), "rb") as bin:
            return bin.read()
    except Exception:
        return b'Error\n'

def hash(key: str):
    h = hashlib.new('sha256')
    h.update(str.encode(key))
    return h.hexdigest()




