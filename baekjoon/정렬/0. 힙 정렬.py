def heap_sort(arr):
    def heapify(idx, heap_size):
        parent = idx
        left = 2 * idx + 1
        right = 2 * idx + 2

        if left < heap_size and arr[left] > arr[parent]:
            parent = left
        if right < heap_size and arr[right] > arr[parent]:
            parent = right

        if parent != idx:
            arr[idx], arr[parent] = arr[parent], arr[idx]
            heapify(parent, heap_size)

    def sort(arr):
        n = len(arr)
        for i in range(n // 2 - 1, -1, -1):
            heapify(i, n)

        for i in range(n - 1, 0, -1):
            arr[0], arr[i] = arr[i], arr[0]

        return arr

    return sort(arr)
