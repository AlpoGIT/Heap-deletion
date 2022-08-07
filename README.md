# Heap-deletion
O(log n) deletion in heap given a heap and the index of the key to delete.

Work in progress...

It's 10 times slower than heapq.heappop(), but still O(log n) if correct, when we delete first values.
e.g. n=10^9

- 0.06480026245117187500 seconds --- for heap_delete()

- 0.00735378265380859375 seconds --- for heapq.heappop()
