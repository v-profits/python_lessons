s = 'C:\d\new'
print(s)

s = 'C:\d\\new'
print(s)

s = r'C:\d\new'
print(s)

s = 'Ry''thon'
print(s)

s = 'Ry'+'thon'
print(s)

s1 = 'Hello, '
s2 = 'world!'
s = s1 + s2
print(s)

name = 'John'
age = 20
print('My name is ' + name + " I'm " + str(age))

print("hi "*5)

s = 'Hello world!'
print(s[0])  # H
print(s[-1])  # !
print(s[-12])  # H
# s[0] = 'h'  # нельзя изменить символ

s = 'Hello world!'
print(s[0:12])  # Hello world!
print(s[-1])  # !
print(s[0:5])  # Hello
print(s[:5])  # Hello
print(s[6:])  # world!
print(s[::2])  # Hlowrd
print(s[::-1])  # !dlrow olleH
print(s[:5] + s[6:])  # Helloworld!