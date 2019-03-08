#!python
from sorting_iterative import is_sorted, bubble_sort, selection_sort, insertion_sort


def merge(items1, items2):
    """Merge given lists of items, each assumed to already be in sorted order,
    and return a new list containing all items in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    ret = []
    # TODO: Repeat until one list is empty
    one_empty = len(items1) == 0
    two_empty = len(items2) == 0

    while not (one_empty or two_empty):
        # TODO: Find minimum item in both lists and append it to new list
        if items1[0] > items2[0]:
            ret.append(items2.pop(0))
        else:
            ret.append(items1.pop(0))
        one_empty = len(items1) == 0
        two_empty = len(items2) == 0
    # TODO: Append remaining items in non-empty list to new list
    if one_empty:
        ret.extend(items2)
    else:
        ret.extend(items1)
    return ret


def split_sort_merge(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each with an iterative sorting algorithm, and merging results into
    a list in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Split items list into approximately equal halves
    items1 = items[:len(items) // 2]
    items2 = items[len(items) // 2:]
    # TODO: Sort each half using any other sorting algorithm
    bubble_sort(items1)
    bubble_sort(items2)

    # TODO: Merge sorted halves into one list in sorted order
    items[:] = merge(items1, items2)

def merge_sort(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each recursively, and merging results into a list in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check if list is so small it's already sorted (base case)
    if len(items) == 1:
        return
    # TODO: Split items list into approximately equal halves
    items1 = items[:len(items)//2]
    items2 = items[len(items)//2:]
    # TODO: Sort each half by recursively calling merge sort
    merge_sort(items1)
    merge_sort(items2)
    # TODO: Merge sorted halves into one list in sorted order
    items[:] = merge(items1, items2)


def partition(items, low, high):
    """Return index `p` after in-place partitioning given items in range
    `[low...high]` by choosing a pivot (middle point of low and high) from
    that range, moving pivot into index `p`, items less than pivot into range
    `[low...p-1]`, and items greater than pivot into range `[p+1...high]`.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Choose a pivot any way and document your method in docstring above
    pivot = items[(high + low) // 2]  # center of selection
    i = low - 1  # beg pointer
    j = high + 1  # end pointer
    # TODO: Loop through all items in range [low...high]
    while True:  # inf loop
        cond = True  # do while
        while cond:
            i += 1
            if items[i] >= pivot or i >= j:
                cond = False
        cond = True
        while cond:
            j -= 1
            if items[j] <= pivot or i >= j:
                cond = False
        if i >= j:
            return j

        items[i], items[j] = items[j], items[i]


def quick_sort(items, low=None, high=None):
    """Sort given items in place by partitioning items in range `[low...high]`
    around a pivot item and recursively sorting each remaining sublist range.
    TODO: Best case running time: ??? Why and under what conditions?
    TODO: Worst case running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check if high and low range bounds have default values (not given)
    if low is None:
        low = 0
    if high is None:
        high = len(items) - 1
    # TODO: Check if list or range is so small it's already sorted (base case)
    if high - low > 0:
        # TODO: Partition items in-place around a pivot and get index of pivot
        pivot = partition(items, low, high)
        # TODO: Sort each sublist range by recursively calling quick sort
        print('left call', low, pivot - 1)
        quick_sort(items, low, pivot - 1)
        print('right call', pivot + 1, high)
        quick_sort(items, pivot + 1, high)
