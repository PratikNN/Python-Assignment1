#9.write a program that computes the net amount of a bank account based on a transaction log from console input.the log form D 100 W 200
net_amt=0
while True:
    line=input(" ").split()
    if not line:
        break
    amt=int(line[1])
    if line[0]== 'D':
        net_amt+=amt
    elif line[0]=='W':
        net_amt-=amt
print(net_amt)


