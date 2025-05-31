class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return
        if data < self.data:
            # add in left subtree 
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)    
        else:
            # add in right subtree   
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def in_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()
        elements.append(self.data)
        if self.right:
            elements += self.right.in_order_traversal()    
        return elements  

    def pre_order_traversal(self):
        elements = []
        elements.append(self.data)
        if self.left:
            elements += self.left.in_order_traversal()
        if self.right:
            elements += self.right.in_order_traversal()   
        return elements   
    
    def post_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()
        if self.right:
            elements += self.right.in_order_traversal()   
        elements.append(self.data)
        return elements   
    
    def search(self, val): 
        if val == self.data:
            return True
        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False
        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False
                    
    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                print("1st")
                return None
            elif self.left is None:
                print("2nd")
                return self.right
            elif self.right is None:
                print("3rd")
                return self.left
            print("xxxx")
            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete(min_val)

        return self

    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()  

def build_binary_tree(elements):
    root = BinarySearchTreeNode(elements[0])
    for i in range(1,len(elements)):
        root.add_child(elements[i])
    return root  


def main():
    arr = [7,6,2,3,7,8,10,9,12,11,10]
    root = build_binary_tree(arr)
    print(root.in_order_traversal())
    # print(root.pre_order_traversal())
    # print(root.post_order_traversal()) 
    # print(root.search(2))
    root.delete(10)
    print(root.in_order_traversal())

if __name__ == "__main__":
    main()