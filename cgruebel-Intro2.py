first = int(input("Please enter first number: "))
second = int(input("Please enter second number: "))
result = ""
for i in range(first, second):
    if i%7==0 and i%5!=0:
        result += str(i)+","

result = result[:-1]

print(result)
