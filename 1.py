#1.write a program which can compute factorial of a given number using recursion.The output should be a ',' seperated value in console
def factorial(n):
    if n==1:
        return n
    else:
        return n*factorial(n-1)
num=int(input("enter a number:"))
if num==0:
    print("factorial of 0 is 1")
else:
    print("factorial of",num,"is :",factorial(num))
