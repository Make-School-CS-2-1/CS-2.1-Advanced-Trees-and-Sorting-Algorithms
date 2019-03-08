#!python


def is_sorted(items):
    """Return a boolean indicating whether given items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check that all adjacent items are in order, return early if so
    last = items[0]
    for num in items:
        if last > num:
            return False
        last = num
    return True


def bubble_sort(items):
    """Sort given items by swapping adjacent items that are out of order, and
    repeating until all items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    while not is_sorted(items):
        # TODO: Swap adjacent items that are out of order
        last = items[0]
        for (i, num) in enumerate(items):
            if last > num:
                items[i] = last
                items[i - 1] = num
            else:
                last = num


def selection_sort(items):
    """Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    unsorted_index = 0
    # TODO: Repeat until all items are in sorted order
    while not is_sorted(items):
        # TODO: Find minimum item in unsorted items
        min_item = (items[unsorted_index], unsorted_index)
        for (i, item) in enumerate(items[unsorted_index:], unsorted_index):
            if item < min_item[0]:
                min_item = (item, i)
        # TODO: Swap it with first unsorted item
        items[min_item[1]] = items[unsorted_index]
        items[unsorted_index] = min_item[0]
        unsorted_index += 1


def insertion_sort(items):
    """Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    unsorted_item = [0, items[0]]
    # TODO: Repeat until all items are in sorted order
    while not is_sorted(items):
        # TODO: Take first unsorted item
        unsorted_item[0] = unsorted_item[0] + 1
        unsorted_item[1] = items[unsorted_item[0]]
        # TODO: Insert it in sorted order in front of items
        for (i, item) in enumerate(items[:unsorted_item[0]]):
            if item > unsorted_item[1]:
                items.insert(i, unsorted_item[1])
                del items[unsorted_item[0] + 1]
                break
            elif i == unsorted_item[0] - 1:
                items.insert(unsorted_item[0], unsorted_item[1])
                del items[unsorted_item[0] + 1]

