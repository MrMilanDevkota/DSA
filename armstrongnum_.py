# armstrong number
# 153= 1^3+5^3+3^3 -> armstrong

n=1634
num=n
arm=0
pow= len(str(num))
while num>0:
    last_digit=num % 10
    # print(last_digit)
    a= ((last_digit)**pow)
    arm= a+arm
    num= num//10

print(arm)
if arm ==n:
    print("armstrong")
else:
    print("not armstrong")


