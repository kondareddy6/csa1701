num=int(input("Enter a number"))
temp=num
Sum=0
while num!=0:
      r=num%10;
      Sum=Sum+r*r*r
      num=num//10

if(temp==Sum):
    print('Armstrong Number')
else:
    print("Not Armstrong Number")

