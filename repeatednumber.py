list=[1,3,4,5,6,6,7,7,7,8]
def function(list):
    repeatedNumber=list[0]
    for i in list:
        if list.count(i)>list.count(repeatedNumber):
            repeatedNumber=i
    print(repeatedNumber)
function(list)

