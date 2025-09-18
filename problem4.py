def isPalindrome(valStr):
    return valStr == valStr[::-1]

def toBinaryIfNumber(value):

    if value.isdigit():
        return bin(int(value))[2:]
    return None

def main():
    user_input = input("Enter a value: ")

    is_input_palindrome = isPalindrome(user_input)

    binary_value = toBinaryIfNumber(user_input)

    if binary_value:
     
