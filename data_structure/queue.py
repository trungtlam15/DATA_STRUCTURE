
class  Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self,item):
        self.queue.append(item)

    def dequeue(self):
        self.queue.pop(0)

if __name__ == '__main__':
    new_queue = Queue()
    new_queue.enqueue(1)
    new_queue.enqueue(2)
    new_queue.enqueue(3)
    new_queue.enqueue(4)
    print(new_queue.queue)

    new_queue.dequeue()
    print(new_queue.queue)

    new_queue.dequeue()
    print(new_queue.queue)

    new_queue.enqueue(10)
    print(new_queue.queue)
