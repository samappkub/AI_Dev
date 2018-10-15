class Stack:
    def __init__(self):
        self.data = []
        self.hashes = []

    def empty(self):
        return len(self.data) == 0

    def push(self, item):
        self.data.insert(0, item)
        self.hashes.append(item[0].config)

    def pop(self):
        return self.data.pop(0)

    def __contains__(self, el):
        return el.config in self.hashes


class Queue:
    def __init__(self):
        self.data = []
        self.hashes = []

    def empty(self):
        return len(self.data) == 0

    def enqueue(self, item):
        self.data.append(item)
        self.hashes.append(item[0].config)

    def dequeue(self):
        return self.data.pop(0)

    def __contains__(self, el):
        return el.config in self.hashes


class PriorityQueue:
    def __init__(self):
        self.data = []
        self.hashes = []

    def put(self, item):
        self.data.append(item)
        self.data.sort(key=lambda x: x[0])
        self.hashes.append(item[1][0].config)

    def get(self):
        return self.data.pop(0)[1]

    def empty(self):
        return len(self.data) == 0

    def __contains__(self, el):
        return el.config in self.hashes
