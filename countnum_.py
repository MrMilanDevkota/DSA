# learning the extraction of digits 
"""
- count digits, reverse a number, check palindrome, armstrong number"""


# idea 1
''' 
# last digit print gareko ra count gareko 
n= 5873
num = n
count=0
while num>0:
    # last_digit= num%10
    # print(last_digit)
    num=num//10
    count += 1
  
print ("The number of digits is:" ,count)
'''

#idea 2
# or idea ko lagi hamle just yesko log10(num) + 1 garey hunxa lets see 
from math import*
def count_digit(num):
    count= int(log10(num)+1)
    return count

print("The number of digit is", count_digit(5873))

# time complexity -> o(log10(n))