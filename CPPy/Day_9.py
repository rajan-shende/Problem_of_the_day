# Check a string is a palindrome without inbuild function:
str1 = "hello"
str2 = "dad"
def is_palindrome(str1):
    list1 = [a for a in str1]
    a =''
    for b in list1:
        a = b + a
    if a == str1:
        print("String is palindrome")
    else:
        print("String is not palindrome")

is_palindrome(str1)
is_palindrome(str2)

# If string is a plindrome with enhanced complexity

def is_palindrome_enhanced(str1):
    start = 0
    end = len(str1) - 1
    while start < end:
        if str1[start] != str1[end]:
            print("string is not a palindrome string")
            return
        start += 1
        end -= 1
    print("string is a plaindrome")

is_palindrome_enhanced("POP")
is_palindrome_enhanced("IMI")
is_palindrome_enhanced("TOP")
