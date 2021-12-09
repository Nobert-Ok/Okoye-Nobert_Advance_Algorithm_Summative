# creating a function that takes in two argument n and k
def superDigit(n,k):
    # initializing the variable total to store the current sum of the 
    # digit in n
    total = 0
    
    # creating a variable p to store the concatenation (n times k)
    # an convert to integers
    p = int(n*k)
    
    # while p is greater than 0 and total is greater than 9,
    # the loop continues to run until it no longer satisfies
    # the constraints
    
    while(p > 0 or total > 9):
        # if p is equal to 0, that means we have finished adding 
        # the current digit and then let's swap our current p with the 
        # total gotten so far to continue searching for the super value
        if(p == 0):
            p,total = total,p
         
        # using the total variable, add the modulo of p to it 
        # and also drop the last digit by dividing it by 10
        else:
            total += p % 10
            p //= 10
        
    # return the total variable
    return total
 
# Test cases
n = '9875'
k = 4
print("n = "+ str(n) +', k = '+ str(k) + ', concatenated value = ' + str(n*k) + " and the superdigit = " + str(superDigit(n,k)))

n = '148'
k = 3
print("n = "+ str(n) +', k = '+ str(k) + ', concatenated value = ' + str(n*k) + " and the superdigit = " + str(superDigit(n,k)))

n = '56345'
k = 6
print("n = "+ str(n) +', k = '+ str(k) + ', concatenated value = ' + str(n*k) + " and the superdigit = " + str(superDigit(n,k)))


