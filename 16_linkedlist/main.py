class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        if self.head is None:
            print("List is empty")
            return     
        itr = self.head
        lList = ""
        while itr:
            lList += f"{itr.data}-->"
            itr = itr.next
        print(f"{lList}None")    

    def length_of_lList(self):
        count = 0
        if self.head is None: 
            return count
        itr = self.head
        while itr is not None:
            count += 1
            itr = itr.next    
        return count
    
    def insert_at_beginning(self, data):
        n = Node(data)
        if self.head is None:
            self.head = n
            return
        n.next = self.head
        self.head = n

    def insert_at_end(self, data):
        n = Node(data)
        if self.head is None:
            self.head = n
            return
        itr = self.head
        while itr.next is not None:
            itr = itr.next
        itr.next = n    

    def insert_at(self, idx, data):
        n = Node(data) 
        if idx < 0 or idx > self.length_of_lList():
            raise Exception("Invalid index value..")
        if idx == 0:
            self.insert_at_beginning(data)
        elif idx == self.length_of_lList():
            self.insert_at_end(data)    
        else:
            count = 0
            itr = self.head
            while count != idx - 1:
                itr = itr.next
                count += 1
            temp = itr.next
            itr.next = n
            n.next = temp

    def remove_at(self, idx):
        count = 0
        itr = self.head
        if idx < 0 or idx > self.length_of_lList():
            raise Exception("Invalid index value..")
        if idx == 0:
            temp = itr.next
            del itr
            self.head = temp
            return  
        while count != idx - 1:
            itr = itr.next
            count += 1
        if idx == self.length_of_lList() - 1:
            itr.next = None
            return
        temp = itr.next.next
        del itr.next
        itr.next = temp

    def create_lList(self, li):
        self.head = None
        for i in li:
            self.insert_at_end(i)    
            
    # @staticmethod
    # def printL():
    #     print("hello")          


def printBruteList():
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)

    n1.next = n2
    n2.next = n3

    print(n1.data)
    print(n1.next.data)
    print(n1.next.next.data)


def main():
    # printBruteList()
    # LinkedList.printL()       

    ll = LinkedList()

    # n1 = Node(1)
    # n2 = Node(2)
    # n3 = Node(3)
    # ll.head = n1
    # n1.next = n2
    # n2.next = n3

    ll.length_of_lList()
    ll.insert_at_beginning(2)
    ll.insert_at_beginning(4)
    ll.insert_at_beginning(6)
    ll.length_of_lList()
    ll.insert_at_end(3)
    ll.insert_at_end(5)
    ll.insert_at_end(7)
    ll.length_of_lList()

    ll.insert_at(6, 23)
    ll.insert_at(7, 53)

    ll.printList()

    ll.remove_at(7)
    
    ll.printList()

if __name__ == "__main__":
    main()