lst = [10, 20, 40, 30]

def get_2max(lst):
    max_val = 0
    sec = 0

    for a in lst:
        if a > max_val:
            sec = max_val      # 👈 important line
            max_val = a
        elif a < max_val and a > sec:
            sec = a

    print(sec)

get_2max(lst)
