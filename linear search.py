# BRUTEFORCE - inefficient
def linear_search(data, target):
    for i, value in enumerate(data):
        if value == target:
            return i

    return -1


data = [4, 5, 2, 7, 1, 8]
target = 1
result = linear_search(data, target)
if result == -1:
    print("Item not found.")
else:
    print(f"Item found at position {result}.")
