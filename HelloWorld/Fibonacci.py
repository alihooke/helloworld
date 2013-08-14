__author__ = 'alihooke'
previous = 1
sum = 0
current = 2
while current<4000000:
    previous=current + previous
    current,previous = previous,current
    if (previous % 2)==0:
        sum=sum + previous

print(sum)
