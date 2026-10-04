x = 5
print(type (x) is int)

x = 5.5
print(type(x)is not float)

x = 20
y = 20
if x is y :
    print("x and y have same identity")

y = 30
if x is not y :
    print("x and y have different identity")