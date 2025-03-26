def heapify(arr, n, i):
    largest = i          # Assume the current node is the largest
    left = 2 * i + 1     # Left child index left = 1 --->> 10
    right = 2 * i + 2    # Right child index right = 2 --->> 3
    
    # Compare with left child
    if left < n and arr[left] > arr[largest]:
        largest = left
    
    # Compare with right child
    if right < n and arr[right] > arr[largest]:
        largest = right
    
    # If largest isn’t the current node, swap and recurse
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap
        heapify(arr, n, largest)  # Recurse on the swapped child

# Test it
arr = [10, 4, 3, 5, 1]
n = len(arr)
heapify(arr, n, 5)  # Heapify starting at root
print(arr)  # Output: [10, 5, 3, 4, 1]