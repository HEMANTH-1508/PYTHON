# to find the mean, median and mode of the given list ?

import statistics

numbers = [1, 2, 3, 4, 5, 5, 6, 6, 6, 7]

mean = statistics.mean(numbers)
print("Mean:", mean)

mode = statistics.mode(numbers)
print("Mode:", mode)

median = statistics.median(numbers)
print("Median:", median)

