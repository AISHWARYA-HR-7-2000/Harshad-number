#harshad number in given range
ll = int(input())
ul = int(input())

for N in range(ll, ul + 1):
    dummy = N
    summ = 0
    while dummy > 0:
        rem = dummy % 10
        dummy //= 10
        summ += rem
    if N % summ == 0:
        print(N)
