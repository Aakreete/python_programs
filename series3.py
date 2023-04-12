# this program is to print -1 , 4, -7, 10, -13, 16, -19
count1 = 1
count2 = 0
a = 5
initialvalue = -1
helpervalue = 0
print(initialvalue)
while count1 <= 7:
    helpervalue = (a*count1+count2)
    if (count1 % 2 == 0):
        initialvalue=(initialvalue-helpervalue)
        print(initialvalue)
    else:
        initialvalue= (initialvalue+helpervalue)
        print(initialvalue)
    count1 = count1+1
    count2 = count2+1
