x=int(input("enter a number :"))
y=int(input("enter a number :"))
z=int(input("enter a number :"))
v=int(input("enter a number :"))
g=int(input("enter a number :"))
f=int(input("enter a number :"))
num = [x,y,z,v,g,f]
value=int(input("enter a value to be searched in the array :"))
number=0

for i in num:
    if value!=num[i-1]:
        continue
    elif value==num[i-1]:
        number =number + 1
print(number)
number=0

