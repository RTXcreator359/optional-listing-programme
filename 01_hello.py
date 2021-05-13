print("Enter (S) for sort, (R) for remove,(A) for append,(Re) for reverse, (P) for pop,(I) for insert") 
print("[2,1,3,9,7,5,8,4]")

a = input("Enter option") 

l1 = [2,1,3,9,7,5,8,4] 
if ("(S)" in a):
    l1.sort() 
    print(l1) 

elif ("(R)" in a):
    l1.reverse() 
    print(l1) 

elif ("(A)" in a):
    b = int(input("Enter number to append."))
    l1.append(b)  
    print(l1)  

elif ("(Re)" in a):
    c = int(input("Enter number to be removed.")) 
    l1.remove(c) 
    print(l1)  

elif ("(P)" in a):
    d = int(input("Enter index of number to be poped.")) 
    l1.pop(d)
    print(l1) 

elif ("(I)" in a):
    e = int(input("Enter index of number to be replaced."))  
    f = int(input("Enter number to replace it."))
    l1.insert(e,f) 
    print(l1)

else:
    print("Invalid option.")




