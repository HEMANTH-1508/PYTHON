# wether the numbers in list are in geometric progression or not-10

def geometric(lst):
    if len(lst) < 3:
        return False

    ratio = lst[1] / lst[0]

    for i in range(2, len(lst)):
        if lst[i] / lst[i-1] != ratio:
            return False

    return True

lst = input("Enter a list of numbers separated by commas: ")
lst = [float(x.strip()) for x in lst.split(",")]
if geometric(lst):
    print("list is in geometric progression.")
    print("COMMON RATIO IS : ",lst[1]/lst[0])
else:
    print("list is not in geometric progression.")

