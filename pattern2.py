n=int(input())
k=n
for i in range(0,n):
    for j in range(0,k):
        print(end=" ")
    k=k-1
    for j in range(n):
        print("*",end=" ")
    print()
    
   
"""
5
     * * * * * 
    * * * * * 
   * * * * * 
  * * * * * 
 * * * * *
"""
    
