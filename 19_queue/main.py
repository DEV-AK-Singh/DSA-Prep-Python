from collections import deque

class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self, value):
        self.buffer.appendleft(value)

    def dequeue(self):
        return self.buffer.pop()

    def size(self):
        return len(self.buffer)

    def is_empty(self):
        return self.size() == 0 

def main():
    q = Queue()
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(50) 
    print(q.dequeue())

if __name__ == "__main__":
    main()