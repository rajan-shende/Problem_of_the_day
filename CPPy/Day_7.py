## a list containing the occurances of string input : "aaabbc" & output : [3,2,1]
def less_complex_counter(input_str):
    input_list = [a for a in input_str]
    print(input_list)
    frequency = {}
    for x in  input_list:
        if x in frequency:
            frequency[x] += 1 
        else:
            frequency[x] = 1
    return [ a for a in frequency.values()]

print(less_complex_counter("hello"))
print(less_complex_counter("aaabbc"))
