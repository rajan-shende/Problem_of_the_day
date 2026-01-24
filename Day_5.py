# Reverse a string from specified index onwards
def reverse_at(str_in, id):
	splited = [a for a in str_in ]
	rev = splited[id:][::-1]
	fwd = splited[:id]
	final = fwd+rev
	return final

print(reverse_at("KILL-BILL",4))
