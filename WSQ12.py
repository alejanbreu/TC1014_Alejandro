
def commondivisor(x,y):
    if x == y:
        return x
    elif x > y:
        answer = commondivisor ((x-y),y)
    else:
        answer = commondivisor (x,(y-x))
    return answer

x = (int(input("Write the first number")))
y = (int(input("Write the second number")))

h = commondivisor(x,y)

print ("The greatest common divisor is:",h)
