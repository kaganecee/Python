import random
coins=int(input("Please enter a coin number..:"))
#I created a variable for each chamber to determine the coins falling on the chambers.
chamberone = 0
chambertwo = 0
chamberthree = 0
chamberfour = 0
chamberfive = 0
chambersix = 0
chamberseven = 0
chambereight = 0
chambernine = 0
chamberten = 0
for coins in range(1,coins+1):#Loop,to do this for every coin.
    inc_dec = 0 #The variable mean is increasing/decreasing
    for leftorright in range(1,10):#This process must be repeated 9 times because down there are 9 rows of nails.
        leftorright = random.randint(0, 1)
        if leftorright==0:#if leftorright variable is equal to 0, that's mean the coin is falling to left in my program.
            inc_dec = inc_dec - 1 #one decreasing of our variable , represents falling left.
        elif leftorright==1:#if leftorright variable is equal to 1, that's mean the coin is falling to right in my program.
            inc_dec = inc_dec + 1 #one increasing of our variable , represents falling right.
    #The increment and decrement process is repeated 9 times to determine which chamber the coin falls into.
    #It determines the coin falling into the chamber by increasing or decreasing the variable by one.
    if inc_dec==+9:#For example if the coin falling right 9 times , coin going to chamber 10.
        chamberten += 1
    elif inc_dec==+7:
        chambernine += 1
    elif inc_dec==+5:
        chambereight += 1
    elif inc_dec==+3:
        chamberseven += 1
    elif inc_dec==+1:
        chambersix += 1
    elif inc_dec==-1:
        chamberfive += 1
    elif inc_dec==-3:
        chamberfour += 1
    elif inc_dec==-5:
        chamberthree += 1
    elif inc_dec==-7:
        chambertwo += 1
    elif inc_dec==-9:
        chamberone += 1
print("Number of coins in chamber 1 is:" ,chamberone)
print("Number of coins in chamber 2 is:",chambertwo)
print("Number of coins in chamber 3 is:",chamberthree)
print("Number of coins in chamber 4 is:",chamberfour)
print("Number of coins in chamber 5 is:",chamberfive)
print("Number of coins in chamber 6 is:",chambersix)
print("Number of coins in chamber 7 is:",chamberseven)
print("Number of coins in chamber 8 is:",chambereight)
print("Number of coins in chamber 9 is:",chambernine)
print("Number of coins in chamber 10 is:",chamberten)
#By taking the chambers into the list, I used the loop to find the maximum value for coin on the list.
chambers=[chamberone,chambertwo,chamberthree,chamberfour,chamberfive,chambersix,chamberseven,chambereight,chambernine,chamberten]
maxcoin=0
for i in chambers:
    if maxcoin<i:
        maxcoin=i
rooms=1#Since there are 10 chambers,in order to print this one under the other I got this by incrementing a variable(rooms).
number=0#I created a new variable to be able to traverse each chamber in the list and incremented 1 for each repetition.
for i in range(maxcoin):
    for j in range(len(chambers)+1):
        if number<10:#The variable , must be less than 10 because the index of our last list member is 9.
            print(rooms,"|"," o |"*chambers[number])
            print("---+"*(maxcoin+1))#This code to print only "---+" , one for each chamber.
        rooms= rooms + 1
        number = number + 1
#The code that subtracts these numbers from 1 up to the maximum number of coins and prints them side by side.
for i in range(1,maxcoin+1):
    print("\t",i,end="")






