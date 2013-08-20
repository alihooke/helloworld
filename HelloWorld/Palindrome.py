__author__ = 'alihooke'

def palindrome(x):
    return x == x[::-1]

x = 0
for i in range(5,0,-1):
    for j in range(i,0,-1):
        if i * j < x:
            break
        if palindrome(str(i*j)):
            x = max(x, i*j)
print(x)

