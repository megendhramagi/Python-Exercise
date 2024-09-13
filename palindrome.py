#check palindrome  by getting user input
a=input("Enter something....\n :")
a1=[]
a2=[]
Tcount=0

for x in range(0,len(a)):
    a1.insert(x,a[x])     # converting the user input into list as separate words

a2=a1.copy()   #copy the list
a2.reverse()   # and reverse the second list

for y in range(0,len(a1)):
    if(a1[y]==a2[y]):  #here we compare the both list values by word by word if the both words are equal, tcount will increase
        Tcount+=1
    else:               #else it break the loop and exit
        break

if(Tcount==len(a1)):       #if the tcount is equal a1 or a2 list count it is palindrome else not
    print("its a palindrome")
else:
    print("not a palindrome")

#just for reference
print("\n",len(a1)," ",Tcount,"  ",a1,"  ",a2)