# uses the find minimum value algorithm
def selection_sort(xs):
    for i in range(len(xs) - 1):  # last value will automatically be sorted that's why we - 1
        # find minimum value in unsorted region
        min_index = i

        for j in range(i + 1, len(xs)):
            # update min_index if the value at j is lower than the current minimum value
            if xs[j] < xs[min_index]:
                min_index = j

        # After finding the minimum value in the unsorted region, swap with the first unsorted value.
        xs[i], xs[min_index] = xs[min_index], xs[i]


xs = [3, 2, 1, 5, 4, -3, -17, 34, -2]
print(xs)
selection_sort(xs)
print(xs)

# A nice Pythonic way to check  a list is sorted
# without relying on using Python's own sorting methods to compare.
print(all(xs[i] <= xs[i + 1] for i in range(len(xs) - 1)))
