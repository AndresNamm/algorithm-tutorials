---
title: "BINARY CONVERSION"
---

# DECIMAL TO BINARY

Decimal number will be divided by 2. Remainder will be added to the right side of the array and the quotient is divided again. This process is repeated until quotient = 0.    
In this way the original number is divided with powers of 2. 

1. Find out if we divide the number by 2 ---- if 1 is left over
2. Find out if we divide the number by 2**2 - if 2 is left over
3. Find out if we divide the number by 2**3 - if 4 is left over 
4. Find out if we divide the number by 2**4 - if 8 is left over 

In this process we have to take account the fact in each phase we are doing the 
dividing with a larger number (by the power of 2) This means that the previous remainders
all summed up could not contribute to that sum beacuse in binary every next element going
from right to left (smaller->larger) is larger than the sum of all previous. 


number=10

dividing=quotient,remainder
1. 10/2 = 5,0
2. 5/2  = 2,1
3. 2/2  = 1.0
4. 1/2  = 0,1



1010 = 1*(2\*\*3)+0*(2\*\*2)+1*(2\*\*1)+0*(2\*\*0)

number=10 
I divide the origininal number by 2 and remove the remainder for the next phase (can be 1 or 0). The remainder will be added to the right side of the  array. This means in next phase the resulting number shows IN INT how many 2-s we have.   
In the next phase we divide the amount of 2-s with to get how many 4-s we have. If one 2 is left over **AND MAX 1 2 CAN BE LEFT OVER** then this is remainder and we add 1 to the left side of the array. 
