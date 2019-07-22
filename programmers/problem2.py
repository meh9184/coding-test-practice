import sys

class Queue():
    def __init__(self, max):
        self.max = max + 1
        self.list = [None] * self.max
        self.size = self.front = self.rear = 0

    def get_size(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.max == self.front-1

    def enqueu(self, data):
        if self.is_full():
            print('full')
            return False

        self.rear += 1
        self.size += 1
        self.list[self.rear] = data

        return True

    def dequeue(self):
        if self.is_empty():
            return False
        print(self.front)
        self.front -= 1
        self.size -= 1
        return self.list[self.front]


def main():

    N, C = sys.stdin.readline().split()

    queue = Queue(int(C))
    print(queue.enqueu('hello'))
    print(queue.enqueu('world'))
    print(queue.enqueu('!'))
    print(queue.dequeue())
    print(queue.get_size())

    # for i in range(int(N)):
    #     command = sys.stdin.readline()
    #
    #     if command == 'SIZE':
    #         print(queue.get_size())
    #     elif command == 'TAKE':
    #         print(queue.dequeue())
    #     elif command.split()[0] == 'OFFER':
    #         print(queue.enqueu(command.split()[1]))

main()