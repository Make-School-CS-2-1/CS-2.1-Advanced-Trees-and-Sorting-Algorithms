#!python


def counting_sort(numbers):
    """Sort given numbers (integers) by counting occurrences of each number,
    then looping over counts and copying that many numbers into output list.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Find range of given numbers (minimum and maximum integer values)
    min = numbers[0]
    max = numbers[0]
    for num in numbers:
      if num < min:
        min = num
      elif num > max:
        max = num
    # TODO: Create list of counts with a slot for each number in input range
    counts = [0] * (max - min + 1)
    # TODO: Loop over given numbers and increment each number's count
    for num in numbers:
      counts[num - min] += 1
    # TODO: Loop over counts and append that many numbers into output list
    input_index = 0
    for i, num in enumerate(counts):
      # print(i, num)
      for j in range(num):
        numbers[input_index] = i + min
        input_index += 1
    # FIXME: Improve this to mutate input instead of creating new output list


def bucket_sort(numbers, num_buckets=10):
    """Sort given numbers by distributing into buckets representing subranges,
    then sorting each bucket and concatenating all buckets in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Find range of given numbers (minimum and maximum values)
    # TODO: Create list of buckets to store numbers in subranges of input range
    # TODO: Loop over given numbers and place each item in appropriate bucket
    # TODO: Sort each bucket using any sorting algorithm (recursive or another)
    # TODO: Loop over buckets and append each bucket's numbers into output list
    # FIXME: Improve this to mutate input instead of creating new output list
