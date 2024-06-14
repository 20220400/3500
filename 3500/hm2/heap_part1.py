def isMaxHeap(heap):
    for i in range(0, len(heap)):
        left = 2 * i + 1
        right = 2 * i + 2

        # Check if left child exists and is greater than the current node
        if left < len(heap) and heap[left] > heap[i]:
            return "IMPOSTER"

        # Check if right child exists and is greater than the current node
        if right < len(heap) and heap[right] > heap[i]:
            return "IMPOSTER"

    return "AINT THAT JUST THE WAY"

heap = [10, 9, 7, 3, 1, 4, 3]
heap2 = [2, 3, 7, 9, 1, 4, 5]


print("this is heap 1: " + str(isMaxHeap(heap)))
print("this is heap 2: " + str(isMaxHeap(heap2)))


#The time complexity for the function is O(n) along with the average case, omega would be O(n)