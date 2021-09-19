def bubble_sort(arr):
    for i in range(len(arr) - 1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j - 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]

def improved_bubble_sort(arr):
    end = len(arr) - 1
    while end > 0:
        last_swap = 0
        for i in range(end):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                last_swap = i
        end = last_swap
