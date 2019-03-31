#reverse a string
myvar = 'hello world!'
newCharList = []
totallength = len(myvar)
i = 1
while i <= totallength:
    print(myvar[-i])
    newCharList.append((myvar[-i]))
    i += 1
print(newCharList)
newvar = ''
newvar = newvar.join(newCharList)
print(newvar)