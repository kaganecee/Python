import random
coins=int(input("Please enter a coin number..:"))
chambers = []
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
for coins in range(1,coins+1):
    inc_dec = 0 #increasing/decreasing
    for leftorright in range(1,10):
        leftorright = random.randint(0, 1)
        if leftorright==0:#if leftorright variable is equal to 0, that's mean the coin is falling to left in my program.
            inc_dec = inc_dec - 1 #one decreasing of our valieble , represents falling left.
        elif leftorright==1:#if leftorright variable is equal to 1, that's mean the coin is falling to right in my program.
            inc_dec = inc_dec + 1 #one increasing of our valieble , represents falling right.
    if inc_dec==+9:
        chamberten+=1
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
print("Number of coins in chamber 1 is...:",chamberone)
print("Number of coins in chamber 2 is...:",chambertwo)
print("Number of coins in chamber 3 is...:",chamberthree)
print("Number of coins in chamber 4 is...:",chamberfour)
print("Number of coins in chamber 5 is...:",chamberfive)
print("Number of coins in chamber 6 is...:",chambersix)
print("Number of coins in chamber 7 is...:",chamberseven)
print("Number of coins in chamber 8 is...:",chambereight)
print("Number of coins in chamber 9 is...:",chambernine)
print("Number of coins in chamber 10 is...:",chamberten)

maxcoin=0
if chambersix>=chamberfive and chambersix>=chamberfour:
    if chambersix>=chamberseven:
        maxcoin=chambersix
elif chamberfive>chambersix and chamberfive>=chamberfour:
    if chamberfive>=chamberseven:
        maxcoin=chamberfive

print(" --+"*10,"\n    |",end="")
for i in range(1,11):
    print("{} ".format(i),end=" ")

for i in range(len(chambers)):
    for j in range(maxcoin):
        print(maxcoin, "  |")
        if chambers[i]>0:
            print("o",end=" ")
            chambers[i]=chambers[i]-1
        else:
            print(" ",end="")


chambers=[chamberone,chambertwo,chamberthree,chamberfour,chamberfive,chambersix,chamberseven,chambereight,chambernine,chamberten]
maxcoin=max(chambers)

number=0
rooms=1
print()
for i in range(maxcoin):
    for j in range(len(chambers)+1):
        if number<10:
            if chambers[number]>0:
                print(rooms,"|"," o |"*chambers[number])
            elif chambers[number]==0:
                print(rooms, "|", "   |" * maxcoin)
            print("---+"*(maxcoin+1))
        rooms=rooms+1
        number = number + 1




