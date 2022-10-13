class Hashtable:
    def __init__(self, num_buckets=3):
        self.buckets = [None] * num_buckets
        self.num_buckets = num_buckets
    
    def __charval(self, ch):
        return ord(ch.lower()) - 97

    def hash(self, key):
        return sum([self.__charval(ch) for ch in key]) % self.num_buckets
    
    def insert(self, key, value):
        bucket = self.hash(key)
        if self.buckets[bucket] is None:
            self.buckets[bucket] = []
        self.buckets[bucket].append((key, value))
    
    def find(self, key):
        bucket = self.hash(key)
        if self.buckets[bucket] is None:
            return None
        for k, v in self.buckets[bucket]:
            if k == key:
                return v
        return None

# write tests for the Hashtable class
ht = Hashtable()
ht.insert('a', 1)
ht.insert('b', 2)
ht.insert('c', 3)
ht.insert('d', 4)
ht.insert('e', 5)
ht.insert('f', 6)
print(ht.buckets)
print(ht.find('a'))
print(ht.find('b'))
print(ht.find('c'))
print(ht.find('d'))
print(ht.find('e'))
print(ht.find('f'))




        