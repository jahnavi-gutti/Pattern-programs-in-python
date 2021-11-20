n=int(input())
k=1
for i in range(0,n):
    for j in range(0,k):
        print(end=" ")
    k=k+1
    for j in range(0,n):
        print("*",end=" ")
    print("\r")


"""5
 * * * * * 
  * * * * * 
   * * * * * 
    * * * * * 
     * * * * *"""
