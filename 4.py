#4.write a program to read a 4-digit binary number and print whether it is divisible by 5 or not
def binaryToDecimal(n):
    return int(n,2)
a=input("enter a 4 digit binary number")
b=binaryToDecimal(a)
print("the decimal form of entered no.is",b)
if(b%5==0):
    print("the enterd number is divisible by 5")
else:
    print("the given number is not divisible by 5")