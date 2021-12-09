# creating the function to take inputs
def nth_sum(n):
    # initializing the total variable to keep track of the 
    # current sum
    total = 0
    
    # looping through the range and adding the index to the 
    # total variable starting from 1 to n+1
    for numbers in range(1,n+1):
        total += numbers
        
    # returning the total sum gotten
    return total
    
# calling the function 
import time
start = time.process_time()
# printing out the input,output and time taken for the algorithm to fully execute
print("Input is 10, Output is: "+ str(nth_sum(10)) + ' and time taken: ' + str(time.process_time() - start)+"secs")
print("Input is 10000,Output is: "+ str(nth_sum(10000)) + ' and time taken: ' + str(time.process_time() - start)+"secs")
print("Input is 1000000,Output is: "+ str(nth_sum(1000000)) + ' and time taken: ' + str(time.process_time() - start)+"secs")
print("Input is 100000000,Output is: "+ str(nth_sum(1000000000)) + ' and time taken: ' + str(time.process_time() - start)+"secs")
