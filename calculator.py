#creating mini calculator using lambda
add= lambda a,b: a+b
sub= lambda a,b: a-b
mul= lambda a,b: a*b
div= lambda a,b: a//b
a,b=eval(input("enter the value of a and b: "))
ch=input("Enter + or- or* or //")
if ch =='+':
    print ('sum is :',add(a,b))
elif ch=='-':
    print('sub is : ',sub(a,b))

elif ch=='*':
    print('mul is : ',mul(a,b))
elif ch=='//':
    print('div is : ',div(a,b))
else :
    print("wrong input")
