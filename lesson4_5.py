from functools import reduce
def my_f(num_1, num_2):
    return num_1 * num_2
print(f"{reduce(my_f, [num for num in range(100, 1001) if num % 2 == 0])}")