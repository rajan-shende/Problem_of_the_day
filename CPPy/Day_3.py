# Reversse the string without reverse function or any built in function
str2 = "hello"
def rev_str(input_str):
	a = ""
	for i in input_str:
		a = i+a 
	return a

print(rev_str(str2))
