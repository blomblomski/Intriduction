myString = 'Hello World!'
myString2 = 'this is my second string'
myString3 = 'this is the third string in the program'
x = 2
y = 5
z = 8

print(myString)
print(x)
print(y)
print(z)


if x > y:
    print('X is the largest')

if z < x:
    print('Z is smaller than x')

if z < x and x > y:
    print('X is smaller than Z but larger than Y')

if x < y and x % 2 == 0:
    print('X is smaller than z and x is even')

if myString > myString2:
    print(len(myString))
else:
    print(len(myString2))


len1 = len(myString)
len2 = len(myString2)
len3 = len(myString3)

if len1 > len2 and len1 > len3:
    print(myString)
elif len2 > len1 and len2 > len3:
    print(myString2)
else:
    print(myString3)