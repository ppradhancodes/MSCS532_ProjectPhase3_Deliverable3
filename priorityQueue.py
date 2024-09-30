class PriorityQueue:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) // 2

    def left_child(self, i):
        return 2 * i + 1

    def right_child(self, i):
        return 2 * i + 2

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def push(self, item, priority):
        self.heap.append((priority, item))
        self._bubble_up(len(self.heap) - 1)

    def pop(self):
        if not self.heap:
            raise IndexError("pop from an empty priority queue")
        if len(self.heap) == 1:
            return self.heap.pop()[1]
        min_item = self.heap[0][1]
        self.heap[0] = self.heap.pop()
        self._bubble_down(0)
        return min_item

    def _bubble_up(self, i):
        parent = self.parent(i)
        if i > 0 and self.heap[i][0] < self.heap[parent][0]:
            self.swap(i, parent)
            self._bubble_up(parent)

    def _bubble_down(self, i):
        min_index = i
        left = self.left_child(i)
        right = self.right_child(i)
        if left < len(self.heap) and self.heap[left][0] < self.heap[min_index][0]:
            min_index = left
        if right < len(self.heap) and self.heap[right][0] < self.heap[min_index][0]:
            min_index = right
        if i != min_index:
            self.swap(i, min_index)
            self._bubble_down(min_index)

    def is_empty(self):
        return len(self.heap) == 0