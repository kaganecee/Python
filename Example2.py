def patternA():
    line = 0
    while line < 10:
        star = 0
        while star <= line :
            print("*",end="")
            star = star + 1
        print("")
        line = line + 1
patternA()
print("Pattern A")
def patternB():
    line = 0
    while line <= 10:
        star = 10
        while line <= star:
            print("*", end="")
            star = star - 1
        print("")
        line = line + 1
patternB()
print("Pattern B")
def patternC():
    line = 0
    while line <= 10:
        blank = 0
        star = 10
        while blank <= line:
            print(" ", end="")
            blank = blank + 1
        while line <= star:
            print("*", end="")
            star = star - 1
        print("")
        line = line + 1
patternC()
print("Pattern C")
def patternD():
    line = 0
    while line <= 10:
        blank = 10
        star = 0
        while line <= blank:
            print(" ", end="")
            blank = blank - 1
        while star <= line:
            print("*", end="")
            star = star + 1
        print("")
        line = line + 1
patternD()
print("Pattern D")

