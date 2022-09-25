from sys import maxsize

def maxSubArray(a, s):
    max_so_for = -maxsize -1 
    max_ending_here = 0
    
    for i in range(0,s):
       max_ending_here = max_ending_here + a[i]
       if max_so_for < max_ending_here:
           max_so_for = max_ending_here
           
       if max_ending_here < 0 :
           max_ending_here = 0
    return max_so_for

a = [-2, -3, 4, -1, -2, 1, 5, -3]
print(maxSubArray(a,len(a)))
        