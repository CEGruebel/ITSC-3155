items = int(input("Number of items: "))
list = dict()

for i in range(items):
    takeInput = input(("Input item and price: "))
temp = takeInput.split(' ')
list[temp[0]] = int(temp[1])
sortList = sorted(list.items(), key = lambda x:x[1], reverse = False)
for i in sortList:
    print(i[0],i[1])