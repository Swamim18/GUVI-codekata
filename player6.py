s1, s2 = input().split()
count = 0
for i in range(len(s1)):
  if s1.count(s1[i]) == s2.count(s2[i]):
    count += 1
if count == len(s1):
  print ("yes")
else:
  print ("no")
