""""Using .remove() method, clear the last element of the list."""

lst = [55, 6, 777, 54, 6, 76, 101, 1, 6, 2, 6]
N = lst[-1]
lst = lst[::-1]
lst.remove(N)
print(lst[::-1])
