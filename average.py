"""If given integers A and C, does there exist an average B that is an integer"""
t = int(input())            
for i in range(t):          
    A, C = map(int, input().split())
    B = int((A+C)//2)
    
    if A%2 == 0 and C%2 == 0:
        print(B)
    elif A%2 != 0 and C%2 != 0:
        print(B)
    else:
        print(-1)








