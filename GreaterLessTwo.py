"""check which number is greater and which is less"""
t = int(input())

for i in range(t):
    A, B = map(int, input().split())
    if A<B:
        print("<")
    elif A>B:
        print(">")
    else:
        print("=")
