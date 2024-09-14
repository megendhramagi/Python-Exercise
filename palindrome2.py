#other method to check palindrome
a=input("Enter some something \n :")
a1=""

for i in range(0,len(a)):
    a1+=a[len(a)-(i+1)]#start concat string in reverse
#if a="car" 1st loop a1+=a[3-1] #2nd loop a1+=a[3-2] #3rd loop a1+=a[3-3] loop end 

print(a," ",a1)
print("palindrome" if a==a1 else "not a palindrome")