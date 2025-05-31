class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX

    def __getitem__(self, key):
        h = self.get_hash(key)
        for ele in self.arr[h]:
            if ele[0] == key:
                return ele[1]

    def __setitem__(self, key, val):
        h = self.get_hash(key)
        found = False
        for idx, ele in enumerate(self.arr[h]):
            if len(ele) == 2 and ele[0] == key:
                self.arr[h][idx] = (key, val)
                found = True
                break        
        if not found:
            self.arr[h].append((key, val)) 

def main():
    ht = HashTable()
    ht["march 6"] = 310
    ht["march 7"] = 420
    ht["march 9"] = 430
    ht["march 17"] = 430
    print(ht["march 6"])
    print(ht.arr)

if __name__ == "__main__":
    main()