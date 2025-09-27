#Alternate harshad number
ll = int(input())
ul = int(input())
c=0
for N in range(ll, ul + 1):
    dummy = N
    summ = 0
    while dummy > 0:
        rem = dummy % 10
        dummy //= 10
        summ += rem
    if N % summ == 0:
        c+=1
        if c%2==0:
            print(N)