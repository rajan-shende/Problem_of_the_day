# GET OCCCOURANCE OF EACH ELEMENT WITHIN A LIST 
def less_complex_counter(input_list):
    frequency = {}
    for x in  input_list:
        if x in frequency:
            frequency[x] += 1 
        else:
            frequency[x] = 1
    print(frequency)

less_complex_counter([10,20,30,30,20,10,10])
