# Strings are anagram OR not 
str1 = "silent"
str2 = "listen"
str3 = "fairy tales"
str4 = "rail saftey"
def is_anagram(str_1, str_2):
    dic1 = {}
    dic2 = {}

    for ch in str_1.replace(" ","").lower():
        if ch in dic1:
            dic1[ch] += 1
        else:
            dic1[ch] = 1

    for ch in str_2.replace(" ","").lower():
        if ch in dic2:
            dic2[ch] += 1
        else:
            dic2[ch] = 1

    if dic1 == dic2:
        return "TWO STRINGS ARE ANAGRAM"
    else:
        return "STRINGS ARE NOT ANAGRAM"


print(is_anagram(str1,str2))
print(is_anagram(str3,str4))
