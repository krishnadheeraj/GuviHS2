def reverse(s):
  str=""
  for i in s:
    str=i+str
  return str
s=input().split()
for i in range(2):
  print(reverse(s[i]), end=" ")
