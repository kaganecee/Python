number=int(input("Please enter a number..:"))
divisiors = []
def findDivisiors(number):
    for i in range(1,number+1):
        if (number % i == 0):
            divisiors.append(i)
    return divisiors


print(findDivisiors(number))
def perfectNumber(number):
    if number==sum(divisiors):
        print("This number is perfect number.")