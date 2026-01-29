list1 = [100, 80, 20, 40, 300000, 50, 20, 4000]

def find_max(in_list):
    large = in_list[0]   # start with first element
    for a in in_list:
        if a > large:
            large = a
    return large

print(find_max(list1))
