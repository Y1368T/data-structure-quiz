def bubble_sort_alphabets(arr):
    n = len(arr)

    for i in range(n):
        s = False

        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                s = True

        if not s:
            break

arr = ['d', 'a', 'c', 'f', 'b', 'e']
bubble_sort_alphabets(arr)
print("Sorted array:", arr)