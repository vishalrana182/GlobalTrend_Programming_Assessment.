class Maxheap:
    def __init__(self):
        self.heap = []

    def remove(self):
        if len(self.heap) == 0:
            return None
        elif len(self.heap) == 1:
            return self.heap.pop()
        _Max = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify_deletion(0)
        return _Max

    def insert(self, i):
        self.heap.append(i)
        self.heapify_insertion(len(self.heap)-1)

    def max_value(self):
        if len(self.heap) == 0:
            return None
        return self.heap[0]

    def heapify_insertion(self, i):
        root = (i-1)//2
        if (i > 0) and (self.heap[i] > self.heap[root]):
            self.heap[i], self.heap[root] = self.heap[root], self.heap[i]
            self.heapify_insertion(root)

    def heapify_deletion(self, i):
        l = 2*i+1
        r = 2*1+2
        largest = i

        if (l < len(self.heap)) and self.heap[l] > self.heap[largest]:
            largest = l
        elif (r < len(self.heap)) and self.heap[r] > self.heap[largest]:
            largest = r

        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self.heapify_deletion(largest)

    def __str__(self):
        return str(self.heap)


def main():
        maxheap = Maxheap()
        while True:
            print("1. insert, 2. delete, 3. max_get, 4. Display Heap")
            n = int(input())
            if n == 1:
                n2 = int(input())
                maxheap.insert(n2)
                print(f"inserted: {n2}")
            elif n == 2:
                if maxheap.remove() is not None:
                    print(f"deleted: {maxheap.remove()}")
                else:
                    print("empty heap")
            elif n == 3:
                if maxheap.max_value() is not None:
                    print(f"max value is {maxheap.max_value()}")
                else:
                    print("heap is empty")
            elif n == 4:
                print(f"heap: {maxheap}")
            elif n < 1 or n > 4:
                print("invalid choice")


if __name__ == "__main__":
    main()
