# Enter your code here. Read input from STDIN. Print output to STDOUT
s={}
for i in range(int(input())):
  op=input()
  if op not in s:
    s[op]=1
  else:
    s[op]=s[op]+1
print(len(s))
for i in s:
  print(s[i],end=" ")
