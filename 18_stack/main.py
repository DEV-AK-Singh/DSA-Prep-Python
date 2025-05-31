from collections import deque

class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, value):
        self.container.append(value)

    def pop(self):
        return self.container.pop()

    def size(self):
        return len(self.container)

    def is_empty(self):
        return self.size() == 0

    def peek(self):
        return self.container[-1]    

def main():
    s = Stack()
    s.push(10)
    s.push(20)
    s.push(50)
    print(s.pop())
    print(s.pop())
    print(s.size())
    print(s.peek())
    print(s.is_empty())
    print(s.pop())
    print(s.is_empty())

if __name__ == "__main__":
    main()