#Print 6th to 10th harshad number
start=6
end=10
c=0
N=1
while c<end:
    dummy = N
    summ = 0
    while dummy > 0:
        rem = dummy % 10
        dummy //= 10
        summ += rem
    if N % summ == 0:
        c+=1
        if c>start:
            print(N)
    N+=1


