#print pyramid  using nested loops
def pyramid (n):
    for i in range(1,n+1):
        for j in range(i,n):
            print(" ",end="")
        for k in range(1,2*i):
            print("*",end="")
        print()    
pyramid(5)