# get surname of all of the cricketers
List1 = ['Mahhendra singh', 'Virat Kohali', 'Rohit sharma']

def get_surname(string_in):
	L2 = string_in.split()
	return L2[1]

print([get_surname(a) for a in List1 ])
