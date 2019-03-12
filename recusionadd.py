# The following problem is a basic example of recursion. I have a number n. Write a code which define the summation upto n.
#Basic Approach
def addnumbers(n):
    sum=0
    for i in range(0,n+1):
        sum=sum+i
    return sum
 
 print(addnumbers(5))
 
 //Output: 15 [0+1+2+3+4+5]
 //range() function take values one less than define arguments
 
 #Recursive Approach
 
 def recursiveaddition(n):
    if n==1:
        return 1
    else:
        return n+recursiveaddition(n-1)


print(recursiveaddition(5))

'''
Here {if n==1 return 1}  called base condition. When the function recursiveaddition(1) it return 1 and teminate.
else portion used for recursion. Intial value of n=5. So in the first iteration {return n+recursiveaddition(n-1)} return 5+recursiveaddition(4)
recursiveaddition(4) called again and in 2nd iteration it will be 5+4+recursiveaddition(3).
3rd iteration 5+4+3+recursiveaddition(2)
4th iteration  5+4+3+2+recursiveaddition(1)
So it get it's base condition and return 1 and terminated
'''
