"""There are 100 questions in a paper.
Each question carries +3 marks for correct answer,
-1 mark is deducted for each incorrect answer,
0 marks for an unattempted question.
It is given that Chef received exactly X marks.
Determine the minimum number of problems Chef marked incorrect."""
t = int(input())            
for i in range(t):          
    X = int(input())
    if X%3 == 0:
        print(0)
    elif (X+1)%3 == 0:
        print(1)
    else:
        print(2)