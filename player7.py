s=list(input())
s[::2],s[1::2]=s[1::2],s[::2]
print("".join(s))
