class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break
 
def lca(root, v1, v2): 
    current = root
    v1_anc = []
    v2_anc = []
    while current: 
        v1_anc.append(current.info)
        if current.info < v1:
            current = current.right
        elif current.info > v1:
            current = current.left
        else:
            break
    current = root
    while current:
        v2_anc.append(current.info)
        if current.info < v2:
            current = current.right
        elif current.info > v2:
            current = current.left
        else:
            break 
    i = 0
    while (i < len(v1_anc) - 1) and (i < len(v2_anc)-1) and (v1_anc[i] == v2_anc[i]):
        i += 1
        if v1_anc[i] == v2_anc[i]:
            continue
        else:
            i -= 1
            break
    return Node(v1_anc[i])

tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

v = list(map(int, input().split()))

ans = lca(tree.root, v[0], v[1])
print (ans.info)
