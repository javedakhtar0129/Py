num1 = []

for i in open("input.txt"):
    num1.append(int(i))

count = 0
num2 = []
x = 0

for T in range(1999):
    if T==1997:
        x = num1[T] + num1[T + 1] + num1[T + 2]
        num2.append(x)
        x = 0
        break
    else:
        x=num1[T]+num1[T+1]+num1[T+2]
        num2.append(x)
        x=0


print(num2[1])
print(len(num2))

for x in range(1997):
    if (num2[x + 1] > num2[x]):
        count += 1


print(count)

