"""return an inputed string in reverse"""
def FirstReverse(strParam):
  a = list(strParam)#turn it into a list
  a.reverse()#reverse the order
  strParam = ''.join(a)#turn it back into a string
  return strParam
print(FirstReverse(input()))
