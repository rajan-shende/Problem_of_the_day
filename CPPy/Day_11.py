# Find out duplicates from given list
l1 = [10,20,30,20,40,30,50]

def get_dupes(in_list):
    dupes = []
    Dp = {}
    for a in in_list:
        if a not in Dp:
            Dp[a] = 1
        else:
            Dp[a] += 1
    for a,b in Dp.items():
        if b > 1:
            dupes.append(a)
    print(dupes)


get_dupes(l1)


#trying go improve this
