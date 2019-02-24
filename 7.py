#7.write a program to read the sentense "Hello World" count number of upper case characters and lower case characters.
string="Hello World"
count1=0
count2=0
for i in string:
    if(i.islower()):
        count1+=1
    elif(i.isupper()):
        count2+=1
print("the number of lower case characters are:",count1)
print("number of upper case characters are:",count2)
