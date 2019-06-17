def value(a): 
    if (a == 'I'): 
        return 1
    if (a == 'V'): 
        return 5
    if (a == 'X'): 
        return 10
    if (a == 'L'): 
        return 50
    if (a == 'C'): 
        return 100
    if (a == 'D'): 
        return 500
    if (a == 'M'): 
        return 1000
    return -1
  
def romanToDecimal(z): 
    res = 0
    i = 0
  
    while (i < len(z)): 
  
        s1 = value(z[i]) 
  
        if (i+1 < len(z)): 
  
            s2 = value(z[i+1]) 
  
            if (s1 >= s2): 
  
                res = res + s1 
                i = i + 1
            else: 
  
                res = res + s2 - s1 
                i = i + 2
        else: 
            res = res + s1 
            i = i + 1
  
    return res 
sw=input()
print(romanToDecimal(sw))
