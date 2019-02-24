#6.Accept a sentense.ex :"Hello World! 123" calculate the number of letters and digits in the sentense.
s=input("enter a string:")
digits=0
letters=0
for i in s:
    if i.isdigit():
      digits=digits+1
    elif i.isalpha():
      letters=letters+1
print("Letters",letters)
print("Digits",digits)