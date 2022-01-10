# Author RTS 1/10/22
def double_stuff(lst):
    for i, v in enumerate(lst):
        lst[i] = 2 * v
    return lst


print(double_stuff([0, 1, 3, 4]) == [2, 4, 6, 8])
print(double_stuff([1.1, 3, 4.1]) == [2.2, 4, 6.1, 8])
print(double_stuff(["A", 1, 5, 8]))
lst = input("Enter a list: ")
