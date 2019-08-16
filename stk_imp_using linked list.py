def push(x):
    stk.append(x)
def pop():
    if len(stk)!=0:
        element=stk.pop()
        print("poppped element is:",element)
    else:
        print("stack is empty")    
def display():
    print("elements are",stk,"stacklength",len(stk))
    print("stack implementation in python using list")
stk=[]
ch=0
while(ch!=3):
    print("1.push 2.pop 3.exit\nenter your choice")
    y=input()
    if y.isdigit():
        ch=int(y)
        if ch==1:
            x=int(input("enter the no:"))
            push(x)
            display()
        elif ch==2:
            pop()
            display()
        elif ch==3:
            break
        else:
            print("invalid")
    else:
        print("it is not a number")
