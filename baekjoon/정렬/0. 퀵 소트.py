def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    lesser, equal, greater = [], [], []

    for num in arr:
        if num < pivot:
            lesser.append(num)
        elif num > pivot:
            greater.append(num)
        else:
            equal.append(num)

    return quick_sort(lesser) + equal + quick_sort(greater)

def improved_quick_sort(arr):
    def sort(low, high):
        if high <= low:
            return

        mid = partition(low, high)
        sort(low, mid - 1)
        sort(mid, high)

    def partition(low, high):
        pivot = arr[(low + high) // 2]

        while low <= high:
            while arr[low] < pivot:
                low += 1
            while arr[high] > pivot:
                high -= 1

            if low <= high:
                arr[low], arr[high] = arr[high], arr[low]
                low += 1
                high -= 1
        return low

    return sort(0, len(arr) - 1)