# Flatten the list
L11 = [10,20,[30,40,50,[60,70],80,90],100]
Expected = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

def flatten_list(input_list):
    flatten = []	
    for a in input_list:
	    if type(a) is list:
		    flatten.extend(flatten_list(a))
	    else:
		    flatten.append(a)
    return flatten

print(flatten_list(L11))
