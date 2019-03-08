#!python

from sorting_iterative import bubble_sort

def find_range(numbers):
  minimum = numbers[0]
  maximum = numbers[0]
  for num in numbers:
    if num < minimum:
      minimum = num
    elif num > maximum:
      maximum = num
  return minimum, maximum

def counting_sort(numbers):
    """Sort given numbers (integers) by counting occurrences of each number,
    then looping over counts and copying that many numbers into output list.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""

    # TODO: Find range of given numbers (minimum and maximum integer values)
    minimum,maximum = find_range(numbers)
    # TODO: Create list of counts with a slot for each number in input range
    counts = [0] * (maximum - minimum + 1)

    # TODO: Loop over given numbers and increment each number's count
    for num in numbers:
      counts[num - minimum] += 1
      
    # TODO: Loop over counts and append that many numbers into output list
    input_index = 0
    for i, num in enumerate(counts):
      for j in range(num):
        numbers[input_index] = i + minimum
        input_index += 1
    # FIXME: Improve this to mutate input instead of creating new output list


def bucket_sort(numbers, num_buckets=10):
    """Sort given numbers by distributing into buckets representing subranges,
    then sorting each bucket and concatenating all buckets in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Find range of given numbers (minimum and maximum values)
    minimum, maximum = find_range(numbers)
    # TODO: Create list of buckets to store numbers in subranges of input range
    buckets = []
    for i in range(num_buckets):
      buckets.append([])
    # TODO: Loop over given numbers and place each item in appropriate bucket
    print(maximum, '-', minimum, '+ 1 = ', maximum-minimum + 1, ' // ', num_buckets, ' = ', (maximum - minimum + 1) // num_buckets)
    for num in numbers:
      print(num //((maximum - minimum + 1) // num_buckets))
      buckets[num //((maximum - minimum + 1) // num_buckets) - 1].append(num)
    print('buckets', buckets)
    # TODO: Sort each bucket using any sorting algorithm (recursive or another)
    for bucket in buckets:
      if len(bucket):
        bubble_sort(bucket)
    # TODO: Loop over buckets and append each bucket's numbers into output list
    input_index = 0
    for bucket in buckets:
      for num in bucket:
        numbers[input_index] = num
        input_index += 1
    # FIXME: Improve this to mutate input instead of creating new output list
