'''
def isPalindrome(user_input):
    i = 0
    isPalindrome = True
    while i < len(user_input) and isPalindrome:
        if user_input[i] != user_input[len(user_input) - 1 - i]:
            isPalindrome = False
        i += 1
    return isPalindrome

def isPalindrome(user_input):
    return user_input == user_input[::-1]

'''

def isPalindrome(user_input):
    for i in range(len(user_input)):
        if user_input[i] != user_input[len(user_input) - 1 - i]:
            return False
    return True

def isPalindrome(user_input):
    palindrome = ""
    for i in range(len(user_input) - 1, -1, -1):
        palindrome += user_input[i]
    return user_input == palindrome

def main():
    user_input = input("Enter a string to check if it is a palindrome (hit enter to stop): ")
    while user_input != "":
        if isPalindrome(user_input):
            print(f"\n{user_input} is a palindrome.\n")
        else:
            print(f"\n{user_input} is not a palindrome.\n")
        user_input = input("Enter a string to check if it is a palindrome (hit enter to stop): ")
        
main()
