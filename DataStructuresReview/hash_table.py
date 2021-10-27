# a python implementation of a hash table (besides build in dict, of course)

from typing import Hashable


class HashTable:
    def __init__(self, size: int=100) -> None:
        self.size = size
        self.table = [[] for x in range(self.size)] # using binning for collisions


    def hash_f(self, key: Hashable) -> int:
        return hash(key) % self.size

    
    def put(self, key, val: int) -> None:
        ii = self.hash_f(key) # location to put value

        # check if key already exists
        for jj in range(len(self.table[ii])):
            if self.table[ii][jj][0] == key:
                self.table[ii][jj] = (key, val)
                return
        
        # key doesn't already exist in this case. Simply append to bin
        self.table[ii].append((key, val))
    

    def get(self, key: Hashable) -> int:
        ii = self.hash_f(key)
        for k, v in self.table[ii]:
            if k == key:
                return v
        return None


ht = HashTable()

ht.put("five", 5)
ht.put("two", 2)
ht.put("twenty five", 25)

assert ht.get("five") == 5
assert ht.get("two") == 2
assert ht.get("twenty five") == 25
assert ht.get("six") is None

# replace val in key
ht.put("two", 22)
assert ht.get("two") == 22

# try different object types
ht.put("test", "stringval")
assert ht.get("test") == "stringval"
ht.put("test", {"nested": "dict"})
assert ht.get("test") == {"nested": "dict"}

ht.put("hashtable", HashTable())
ht.get("hashtable").put("nestedhashkey", "myvalue")
assert ht.get("hashtable").get("nestedhashkey") == "myvalue"