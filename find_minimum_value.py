def find_min(xs):
    min_index = 0

    for i in range(len(xs)):
        if xs[i] < xs[min_index]:
            min_index = i
    return xs[min_index]


xs = [3, 2, 6, 9, 7, 4]
print(find_min(xs))
