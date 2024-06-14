def insert_min_heap(heap, value):
    # Add the new element to the end of the heap
    heap.append(value)
    # Get the index of the last element
    index = len(heap) - 1
    # Compare the new element with its parent and swap if necessary
    while index > 0 and heap[(index - 1) // 2] > heap[index]:
        heap[index], heap[(index - 1) // 2] = heap[(index - 1) // 2], heap[index]
        # Move up the tree to the parent of the current element
        index = (index - 1) // 2


def merge_sorted_lists(list1, list2):
    result = []
    min_heap = []

    # Insert the first element from each list into the min-heap
    for i, lst in enumerate([list1, list2]):
        if lst:
            insert_min_heap(min_heap, (lst[0], i, 0))

    while min_heap:
        val, lst_index, idx = min_heap[0]
        result.append(val)

        # Remove the smallest element from the min-heap
        min_heap.pop(0)

        # If there are more elements in the current list, insert the next one into the min-heap
        if idx + 1 < len([list1, list2][lst_index]):
            insert_min_heap(min_heap, ([list1, list2][lst_index][idx + 1], lst_index, idx + 1))

    return result

# Example usage:
list1 = [1, 3, 5, 7]
list2 = [2, 4, 6, 8]
merged_list = merge_sorted_lists(list1, list2)
print(merged_list)
