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
        is_binary_palindrome = isPalindrome(binary_value)
    else:
        is_binary_palindrome = None
    print(f"Input is a palindrome: {is_input_palindrome}")

    if binary_value:
        print(f"Binary equivalent: {binary_value}")
        print(f"Binary is a palindrome: {is_binary_palindrome}")
    else:
        print("No binary conversion since input is text")

if __name__ == "__main__":
    main()