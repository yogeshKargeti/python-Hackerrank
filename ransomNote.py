def check(str1,str2):
  s=list(str1.split())
  p=list(str2.split())
  for i in p:
    if i in s:
      s.remove(i)
    else:
      return "not possible"
  return "possible"

str1=input("Enter first: ")
str2=input("Enter second: ")
t=check(str1,str2)
print(t)