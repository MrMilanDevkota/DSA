# how to reverse a number
# check a palindrome 
n=121
num=n
rev=0
while num>0:
    last_digit= num%10
    num=num//10
    # print(last_digit)
    rev = rev * 10 + last_digit
    print(rev)

if rev==n:
    print("palindrome")
else:
    print("notpalindrome")
