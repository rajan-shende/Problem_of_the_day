# CASE 1
# Find out all letters commmon in given two strings

# CASE 2 
# Find out letters which are present in first string and not present in the second string

str1 = 'Hello'
str2 = 'heLLo'

# Solution 1 
# for common letters using inbuilt methods
def find_common_characters(str1, str2):
    s1 = set(a for a in str1)
    s2 = set(a for a in str2)
    return list(s1.intersection(s2))

# Solution 2 
# for common letetrs using traditional implementation
def find_common_characters_2(str1, str2):
    s1 = set(a for a in str1)
    s2 = set(a for a in str2)
    common = []
    for a in s1:
        if a in s2:
            common.append(a)
    return common

print(find_common_characters(str1,str2))
print(find_common_characters_2(str1,str2))


def check_viceversa_elements(str1,str2):
    s1 = set(a for a in str1)
    s2 = set(a for a in str2)
    print("\nFIRST STRING IS {}\n\nSECONDS STRING IS {}\n".format(str1,str2))
    print("ELEMENTS PRESENT IN STRING 1 AND NOT IN STRING 2\n")
    print(list(s1.difference(s2)))
    print("ELEMENTS PRESENT IN STRING 2 AND NOT IN STRING 1\n")
    print(list(s2.difference(s1)))


check_viceversa_elements(str1,str2)
