class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX

    def __getitem__(self, key):
        h = self.get_hash(key)
        return self.arr[h]

    def __setitem__(self, key, val):
        h = self.get_hash(key)
        self.arr[h] = val

def main():
    ht = HashTable()
    ht["march 6"] = 310
    ht["march 7"] = 420
    ht["march 8"] = 430
    # print(ht["march 6"])
    # print(ht.arr) 

if __name__ == "__main__":
    main()