#Print first n harshad number
target= int(input())
c=0
N=1
while c<target:
    dummy = N
    summ = 0
    while dummy > 0:
        rem = dummy % 10
        dummy //= 10
        summ += rem
    if N % summ == 0:
          print(N)
          c+=1
    N+=1