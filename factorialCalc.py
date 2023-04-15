"""calculate a factorial"""
def FirstFactorial(num):
  integer = num - 1
  for i in range(integer):
    num = num*(i+1)
  return num
print(FirstFactorial(input()))