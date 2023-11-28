def takeinput():
    x=float(input("Enter First Number: "))
    print("Number 1: ",x)
    y=float(input("Enter Second Number: "))
    print("Number 2: ",y)
    z=str(input("Enter Operation: "))
    print("Your operation: ",z)
    return x,y,z

    
def diplayresult():
    x,y,z=takeinput()
    if z=="+":
        ans=x+y
        print("Ans: ",ans)    
    
    elif z=="-":
        ans=x-y
        print("Ans: ",ans) 
    
    elif z=="*":
        ans=x*y
        print("Ans: ",ans) 
    
    elif z=="/":
        ans=x/y
        print("Ans: ",ans) 
    else:
        print("You Entered the wrong operator!")
        
diplayresult()