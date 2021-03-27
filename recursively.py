number = int(input("Please enter a number..(If you want to exit program enter -1):"))
def factorialFunction(number):
    factorial=1
    while number != -1:
        for i in range(1,number+1):
            factorial=factorial*i
        print(factorial)
        number = int(input("Please enter a number..(If you want to exit program enter -1):"))
factorialFunction(number)