number = int(input("Please enter a 5 digit number..:"))

def isPalindrome(number):
    digit1 = number // 10000
    digit2 = (number // 1000) % 10
    digit3 = (number // 100) % 10
    digit4 = (number // 10) % 10
    digit5 = number % 10
    if (digit1==digit5 and digit2==digit4):
        print("This number is palindrome number.")
    else:
        print("This number is not palindrome number.")
isPalindrome(number)
