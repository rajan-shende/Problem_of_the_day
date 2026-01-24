# Move all 0 to end of the list
list_z = [10,0,20,30,0,40,0,50]

def move_zeros(input_list):
	zeros = []
	non_zeros = []
	for a in input_list:
		if a == 0:
			zeros.append(a)
		else:
			non_zeros.append(a)
	non_zeros.extend(zeros)
	return non_zeros
	
print(move_zeros(list_z))
