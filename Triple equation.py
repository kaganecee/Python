a=0
b=0
def combinations(a,b):
    for a in range(1, 9):
        for b in range(1, 10 - a):
            if a * b * (10 - a - b) == 30:
                print("first""\t""second""\t""third""\t""sum""\t""\t""multiplication")
                print("-----""\t""------""\t""------""\t""----""\t""-------------")
                print(" ",a, "\t  ",b, "\t ",10-a-b, "\t",a+b+(10-a-b), "\t""\t",a*b*(10-a-b), "\t")
combinations(a,b)