#5.write a program which finds all such numbers between 1000 to 3000 such that each digit of the number is even.result should be alist
a=[]
for i in range(1000,3001):
    w=i
    forth=i%10#getting last digit
    nw=i//10#removing last digit
    if(forth%2==0):
        third=nw%10
        nw=nw//10
        if(third%2==0):
            second=nw%10
            nw=nw//10
            if(second%2==0):
                first=nw%10
                if(first%2==0):
                    a.append(w)
print(a)




