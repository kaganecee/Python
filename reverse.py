number=int(input("Please enter a number..:"))
def func(number):
    reverse = 0
    while(number>0):
        digit=number%10
        reverse=reverse*10+digit
        number=number//10
    return reverse
print("Reverse of the number:",func(number))