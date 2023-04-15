"""In Chefland, each chicken has X legs and each duck has Y legs.
Chef's farm can have exactly one type of bird.
Given that the birds on the farm have a total of Z legs:

Print CHICKEN, if the farm can have only chickens but not ducks.
Print DUCK, if the farm can have only ducks but not chickens.
Print ANY, if the farm can have either chickens or ducks.
Print NONE, if the farm can have neither chickens nor ducks."""
t = int(input())            
for i in range(t):          
    X, Y, Z = map(int, input().split())
    
    if (Z%X == 0) and (Z%Y == 0):
        print('ANY')
    elif (Z%X == 0):
        print('CHICKEN')
    elif (Z%Y == 0):
        print('DUCK')
    else:
        print('NONE')