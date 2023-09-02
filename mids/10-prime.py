# 11. Print first 10 prime numbers.

k=30

for i in range(2,k+1):  
    x=0

    for j in range(2, (i//2)+1):  
        if(i%j == 0):  
            x += 1

    if(x<=0):  
        print(i, end=" ")